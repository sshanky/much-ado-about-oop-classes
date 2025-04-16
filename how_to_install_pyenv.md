
# How to install Pyenv

### 💡 What `pyenv` Does (Plain English + Command Examples)
Here’s a breakdown of what `pyenv` helps with and the commands you’ll use:

#### 1. **Install `pyenv` itself**

It works by **shimming** the `python` and `python3` commands to point to your custom-installed versions instead of the system one.

`brew install pyenv`
#### 2. **Set up your shell to use `pyenv`**

Add this to your `~/.zshrc` (or `~/.bash_profile` if using Bash):

### ✅ Where to Add `pyenv` Setup in `.zshrc` 

To ensure `pyenv` works **correctly and consistently**, you should add the two `eval` lines **after** your `oh-my-zsh` is loaded (i.e., after this line):
`source $ZSH/oh-my-zsh.sh`

🔧 So Add This **Right Below** That Line:

```
# Initialize pyenv (add this after Oh My Zsh is sourced)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```
### 🧠 Breakdown of What Each Line Does

| Line                                  | What it does                                                                                                          |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `export PYENV_ROOT="$HOME/.pyenv"`    | Tells your shell where `pyenv` is installed.                                                                          |
| `export PATH="$PYENV_ROOT/bin:$PATH"` | Makes sure the `pyenv` command is available from the terminal.                                                        |
| `eval "$(pyenv init --path)"`         | Ensures `pyenv` sets the right version of Python early in shell startup (important for scripts and login shells).<br> |
| eval "$(pyenv init -)"                | Finalizes `pyenv` setup for interactive shell sessions (like when you’re typing commands).                            |

📌 After Editing `.zshrc`
To activate the changes, run:
`source ~/.zshrc`



Now that's all present and installed correctly to play nice with your .zshrc
You can now safely play around with installing and using different versions of Python.
#### 3. Now if you wanted to **Install a new Python version** you have several options on how and what and where you want to do so.

I've created a table that goes over the 3 different ways you can now install python versions. 

## 🧩 The Three Related But Distinct Concepts

| Command                   | Purpose                                                            | Where it Applies                                      | What It Actually Does                                                       |
| ------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------- | --------------------------------------------------------------------------- |
| `pyenv install <version>` | **Installs** a Python version                                      | Globally on your system (inside `~/.pyenv/versions/`) | Downloads, compiles, and installs Python version. **Does not activate it.** |
| `pyenv global <version>`  | **Sets the default version** used everywhere (unless overridden)   | Globally for your whole shell/user                    | Updates a file at `~/.pyenv/version`                                        |
| `pyenv local <version>`   | **Sets the Python version just for the current directory/project** | Only in the current directory and subdirs             | Creates a `.python-version` file here                                       |

 ### 🚨It should be noted that pyenv can also be used to *uninstall* python version as well.🚨
 `pyenv uninstall 3.12.1

### 🗺️ Here's a Real-World Analogy

Think of it like this:

- 🛠️ **`pyenv install`** = “Buy and store a tool in your workshop.” (But don’t use it yet.)
    
- 🌐 **`pyenv global`** = “This is my go-to tool I’ll use _everywhere_.”
    
- 🗂️ **`pyenv local`** = “In _this_ project, I want to use _this specific tool_.”
---

### 🔍 Check What You're Using

You can always see which Python version you’re _actually_ using by running:
`python --version`
`python3 --version` 
`which python` 
`which python3`

And once `pyenv` is active:
`pyenv versions

This shows all installed versions and which one is active.

And you can check what python versions you currently have available to you; that you've installed with:

`ls ~/.pyenv/versions

### 🚀 TL;DR

You _do_ have Python (yay!). But yes, for **serious Python work**, `pyenv` is the recommended way to manage versions cleanly and safely—especially on macOS.