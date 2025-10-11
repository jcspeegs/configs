function thumbnail_extractor --description "Extract a thumbnail from a video"
    argparse --min-args=1 --max-args=1 'h/help' 's/source-frame=?' 'i/input=' -- $argv
    or return

    # Help
    if set -ql _flag_h
        echo "Usage: thumbnail_extractor [-h | --help] [-s | --source-frame=SOURCE] [-i | --input] THUMBNAIL_FILENAME" >&2
        return 1
    end

    # Source frame
    if not set -ql _flag_s
        set _flag_s "00:00:30"
    end

    # Input file
    if not set -ql _flag_i
        echo "Error: -i is a required option" >&2
        return 1
    end

    # Output file
    set output_file $argv[1]

    ffmpeg -ss $_flag_s -i $_flag_i -frames:v 1 $output_file

end
