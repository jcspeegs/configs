" See :h defaults
unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim

filetype on
filetype plugin on
filetype indent on
syntax on

let python_highlight_all=1

" Use hybrid line numbers
set relativenumber number

" tab == 4 spaces
set tabstop=4 softtabstop=4
set shiftwidth=4
set textwidth=79
set expandtab smarttab
set autoindent smartindent

au BufNewFile,BufRead *.yaml
    \ set tabstop=2 softtabstop=2 shiftwidth=2

" Enable wild menu file search
set wildmenu
set wildignore+=*.swp,*.zip,*/.git/*

set showmatch
set linebreak

set ignorecase smartcase

"set foldmethod=syntax
"set foldmethod=indent
set incsearch
"set noswapfile

set undodir=~/.vim/undodir
set undofile

set colorcolumn=80
highlight ColorColumn guibg=lightgrey

colorscheme gruvbox
set background=dark

" Set leader to space
let mapleader = "\<space>"
nmap <leader>/ :nohlsearch<cr>| "Clear search highlight

nnoremap <silent> <Space> @=(foldlevel('.')?'za':"\<Space>")<CR>

" ctrl-p toggles line nums / rel nums
nnoremap <C-p> :set nu! \| :set rnu!<CR>

" Window navigation
" leader-X instead of ctrl-wX or ctrl-X
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" Natural split openning
"  Open new split panes to tthe right and bottom
set splitbelow splitright

" undotree
nnoremap <leader>u :UndotreeToggle<CR>

" Commentary
autocmd FileType sas setlocal commentstring=/*\ %s\ */

" FZF
" List of commands: https://github.com/junegunn/fzf.vim
set rtp+=/usr/bin/fzf

" [Buffers] Jump to the existing window if possible
let g:fzf_buffers_jump = 1

nnoremap <silent> <leader>f :FZF<CR>| "Search files current directory
nnoremap <silent> <leader>r :History<CR>| "Search recent files
nnoremap <silent> <leader><space> :Rg<CR>| "Search in project files

command! -bang FZFHome call fzf#vim#files('~', <bang>0)
nnoremap <silent> <leader>h :FZFHome<CR>| "Search files in home

nnoremap <silent> <F1> :Helptags<CR>

" NERDTree
" map NERDTree toggle
map <C-n> :NERDTreeToggle<CR>
" open NERDTree on vim start up
"autocmd vimenter * NERDTree

" close vim if only NERDTree window is open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
 
" Vim Airline
set laststatus=2
set t_Co=256
let g:airline_powerline_fonts = 1

" Smarter tab line
let g:airline#extensions#tabline#enabled = 1
let g:gruvbox_contrast_dark='medium'

" Airline Theme
"let g:airline_theme='molokai'
let g:airline_theme = 'gruvbox'
"let g:airline_theme = 'bubblegum'
