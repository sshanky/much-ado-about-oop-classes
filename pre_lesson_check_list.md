# ✅ Pre-Lesson Setup Checklist
Before you clone this repository and dive into learning about classes and object-oriented programming in Python, 
it’s a good idea to make sure your system is set up and ready to roll. 
This checklist will help you verify a few important things first.

### 1. 🛠️ Do You Have Git Installed?
The easiest way to check is by running:

```
which git
```

#### 🧠 What does this do?
The `which` command checks your system’s `$PATH` to see where the executable file for a given command lives—if it exists at all.

💡 
>When in doubt, man page it out:
>Try man w

#### ✅ Example output:

```
☁ ~ which git
/usr/bin/git
```
If you get something like the above, awesome—Git is installed! If not, you’ll want to install Git first.

### 2. 🧾 Do You Have Git Configured?
You’ll want to make sure your identity is set up so your commits are properly tracked.

#### 🔍 Check your global Git config:

```
git config --global --list
```

You should see something like:

```
user.name=Your Name
user.email=you@example.com
```

If not, you can set them using:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
> The --global flag means this will apply to all repos unless a specific one overrides it.

#### 🧹 Do You Have a Global .gitignore File?
A global .gitignore helps you ignore files across all your repos—like .DS_Store, log files, etc.

Check if you have one set up:

```
git config --get core.excludesfile
```
- If nothing is returned, you don’t have one (yet!).

- If a path is returned, you can open it with:

```
nano /path/to/your/global/.gitignore
```

### 3. 🐍 Are You Using the Right Version of Python?
Most macOS systems come with Python pre-installed, but often you'll need to explicitly use python3.

#### 🧪 Check your Python version:
```
python3 --version
```
**Example output**:
```
☁ ~ python3 --version
Python 3.9.6
```
If you don't get output from python --version, don’t worry—that’s normal on macOS.

#### 💡 Pro Tip: Install pyenv
If you want flexibility to switch between Python versions easily, consider installing [pyenv](https://github.com/pyenv/pyenv)

**It lets you**:

- Install and manage multiple versions of Python.

- Set a specific version globally or per-project.

- Keep your dev environments clean and conflict-free.

If that interests you, check out [How to Install pyenv](how_to_install_pyenv.md)