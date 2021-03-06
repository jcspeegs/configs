" See :h defaults
unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim

filetype on
syntax on

" Use hybrid line numbers
set relativenumber number

" tab == 4 spaces
set tabstop=4 shiftwidth=4 expandtab smarttab
set autoindent

" Enable wild menu file search
set wildmenu

set showmatch
set linebreak

set ignorecase smartcase

set foldmethod=indent

nnoremap <silent> <Space> @=(foldlevel('.')?'za':"\<Space>")<CR>

" ctrl-p toggles line nums / rel nums
nnoremap <C-p> :set nu! \| :set rnu!<CR>

" Window navigation
" ctrl-j instead of ctrl-wj
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Natural split openning
"  Open new split panes to tthe right and bottom
set splitbelow splitright

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

" Airline Theme
let g:airline_theme='molokai'
