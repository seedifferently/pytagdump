================================================================================
pytagdump v0.2
================================================================================

| Copyright: (c) 2011 Seth Davis
| http://github.com/seedifferently/pytagdump


Synopsis
================================================================================

pytagdump is a simple utility to print the ID3/tag info of various files
supported by the "mutagen" package.


Installation
================================================================================

To install, simply::

    pip install http://github.com/seedifferently/pytagdump/zipball/master

* You'll need to have `Python`_ 2.5+ and `pip`_ installed.
* You might have to be root (or use sudo) for pip to install the script into a
  globally executable directory in your $PATH.
* pip should automatically install mutagen for you, but the advanced user can
  find it here: http://code.google.com/p/mutagen/

.. _Python: http://www.python.org
.. _pip: http://www.pip-installer.org


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

    -j/--json       Dump tag info in the JSON format (make sure you have Python
                    v2.6+ or have installed the JSON package).
    -y/--yaml       Dump tag info in the YAML format (make sure you have
                    installed the PyYAML package).
    -i/--info       Include additional info (bitrate, length, etc) in tag dump.
    -v/--verbose    Print additional informational messages.


Disclaimers and Warnings
================================================================================

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
