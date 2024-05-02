# Job Alerter :)

Simple job alerter, that using full alerting system for new jobs

## Usage

### Create virtualenvironment

Install venv library to create virtual environment

$ ``` python -m pip install venv ```

create virtualenvironment

$ ``` python -m venv .venv ```

active virtualenvironment

in linux:

$ ``` source .venv/bin/activate ```

in windows(Powershell):

``` .venv/Scripts/activate.ps1 ``` or (Batch) ``` .venv/Scripts/activate.bat ```

### install requirements

``` pip install -r requirements.txt ```



% ### Setting Email and Password

% #### <span>Linux, macOS</span>
% ```
% export EMAIL=Your_Email@gmail.com
% export PASSWORD=Your_Password
% ```

% #### <span>Windows</span>
% ```
% set EMAIL=Your_Email@gmail.com
% set PASSWORD=Your_Password
% ```

% % <span>After You've Set Email and Password, please run this command befor running main project</span>
% ```
% python auth.py
```
<span>then</span>
```
python main.py
```