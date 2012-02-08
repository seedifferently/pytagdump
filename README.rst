================================================================================
pytagdump v0.3.1
================================================================================

| Copyright: (c) 2012 Seth Davis
| http://github.com/seedifferently/pytagdump


Synopsis
================================================================================

pytagdump is a simple utility to print the ID3/tag info of various files
supported by the "mutagen" package.


Installation
================================================================================

To install, simply::

    pip install pytagdump

* You'll need to have `Python`_ 2.5+ and `pip`_ installed.
* You might have to be root (or use sudo) for pip to install the script into a
  globally executable directory in your $PATH.
* For JSON output support, make sure you have at least Python v2.6 (or
  install the `simplejson` package for Python v2.5).
* For YAML output support, make sure you install the `PyYAML` package.
* Optonally, you can use pip's `setuptools extras`_ syntax to have either (or
  both) of these packages automatically installed for you. e.g. `pip install
  pytagdump[JSON,YAML]`
* pip should automatically install mutagen for you, but the advanced user can
  find it here: http://code.google.com/p/mutagen/

.. _Python: http://www.python.org
.. _pip: http://www.pip-installer.org
.. _setuptools extras: http://peak.telecommunity.com/DevCenter/setuptools
                       #declaring-extras-optional-features-with-their-own-
                       dependencies


Usage
================================================================================

::

    pytagdump [OPTIONS] file(s)


Examples
--------------------------------------------------------------------------------

::

    pytagdump [OPTIONS] ~/Music/*.mp3

or::

    pytagdump [OPTIONS] "~/Music/Rick Astley - Never Gonna Give You Up.mp3"


Options
================================================================================

::

    -j/--json       Dump tag info in the JSON format.
    -y/--yaml       Dump tag info in the YAML format.
    -i/--info       Include additional meta info (bitrate, length, etc) in tag
                    dump.
    -s/--size       Include file size (in bytes) in tag dump.
    -v/--verbose    Print additional informational messages.


Disclaimers and Warnings
================================================================================

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
