call plug#begin()
Plug 'tomasiser/vim-code-dark'
Plug 'sheerun/vim-polyglot'
Plug 'preservim/nerdtree'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
"Plug 'jackguo380/vim-lsp-cxx-highlight'
Plug 'bfrg/vim-cpp-modern'
call plug#end()


" Learn VimScriptTheHardWay
" MAPPING
"
" move line up and down
nnoremap - ddp
nnoremap _ kddpk

" uppercase current word
inoremap <c-u> <esc>viwU<esc>ea


"set t_Co=256
colorscheme codedark
set number
set shiftwidth=4
set tabstop=4
set expandtab
set nowrap
set incsearch
set ignorecase
set smartcase
set showmode
set showmatch
set hlsearch

nnoremap <C-n> :NERDTree<CR>


" Disable function highlighting (affects both C and C++ files)
let g:cpp_function_highlight = 1

" Enable highlighting of C++11 attributes
let g:cpp_attributes_highlight = 1

" Highlight struct/class member variables (affects both C and C++ files)
let g:cpp_member_highlight = 1

" Put all standard C and C++ keywords under Vim's highlight group 'Statement'
" (affects both C and C++ files)
let g:cpp_simple_highlight = 1
