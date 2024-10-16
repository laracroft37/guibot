# Copyright 2013-2018 Intranet AG and contributors
#
# guibot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# guibot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with guibot.  If not, see <http://www.gnu.org/licenses/>.

"""
Global and local (per target or region instance) configuration.

SUMMARY
------------------------------------------------------


INTERFACE
------------------------------------------------------

"""

import logging
from typing import Any

from .errors import *


log = logging.getLogger("guibot.config")


class Config:
    """
    Metaclass used for the definition of static properties (the settings).

    We overwrite the name of the class in order to avoid documenting
    all settings here and adding an empty actual class. Instead, the resulting
    documentation contains just the config class (using this as metaclass)
    and all settings respectively. In this way the front user should not worry
    about such implementation detail and simply use the provided properties.

    For those that like to think about it nonetheless: All methods of the
    resulting config class are therefore static since they are methods of
    a class object, i.e. a metaclass instance.
    """

    def __init__(self) -> None:
        """Operational parameters shared between all instances."""
        self.toggle_delay = 0.05
        self.click_delay = 0.1
        self.drag_delay = 0.5
        self.drop_delay = 0.5
        self.keys_delay = 0.2
        self.type_delay = 0.1
        self.rescan_speed_on_find = 0.2
        self.wait_for_animations = False
        self.smooth_mouse_drag = True
        self.screen_autoconnect = True
        self.preprocess_special_chars = True
        self.save_needle_on_error = True
        self.image_logging_level = logging.ERROR
        self.image_logging_destination = "imglog"
        self.image_logging_step_width = 3
        self.image_quality = 3

        # backends shared between all instances
        self.display_control_backend = "pyautogui"
        self.find_backend = "hybrid"
        self.contour_threshold_backend = "adaptive"
        self.template_match_backend = "ccoeff_normed"
        self.feature_detect_backend = "ORB"
        self.feature_extract_backend = "ORB"
        self.feature_match_backend = "BruteForce-Hamming"
        self.text_detect_backend = "contours"
        self.text_ocr_backend = "pytesseract"
        self.deep_learn_backend = "pytorch"
        self.hybrid_match_backend = "template"

    def toggle_delay(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: time interval between mouse down and up in a click
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._toggle_delay
        else:
            self._toggle_delay = value
            return None

    #: time interval between mouse down and up in a click
    toggle_delay = property(fget=toggle_delay, fset=toggle_delay)

    def click_delay(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: time interval after a click (in a double or n-click)
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._click_delay
        else:
            self._click_delay = value
            return None

    #: time interval after a click (in a double or n-click)
    click_delay = property(fget=click_delay, fset=click_delay)

    def delay_after_drag(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: timeout before drag operation
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._drag_delay
        else:
            self._drag_delay = value
            return None

    #: timeout before drag operation
    delay_after_drag = property(fget=delay_after_drag, fset=delay_after_drag)

    def delay_before_drop(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: timeout before drop operation
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._drop_delay
        else:
            self._drop_delay = value
            return None

    #: timeout before drop operation
    delay_before_drop = property(fget=delay_before_drop, fset=delay_before_drop)

    def delay_before_keys(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: timeout before key press operation
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._keys_delay
        else:
            self._keys_delay = value
            return None

    #: timeout before key press operation
    delay_before_keys = property(fget=delay_before_keys, fset=delay_before_keys)

    def delay_between_keys(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: time interval between two consecutively typed keys
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._type_delay
        else:
            self._type_delay = value
            return None

    #: time interval between two consecutively typed keys
    delay_between_keys = property(fget=delay_between_keys, fset=delay_between_keys)

    def rescan_speed_on_find(self, value: float = None) -> float | None:
        """
        Get or set property attribute.

        :param value: time interval between two image matching attempts
                      (used to reduce overhead on the CPU)
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._rescan_speed_on_find
        else:
            self._rescan_speed_on_find = value
            return None

    #: time interval between two image matching attempts (used to reduce overhead on the CPU)
    rescan_speed_on_find = property(
        fget=rescan_speed_on_find, fset=rescan_speed_on_find
    )

    def wait_for_animations(self, value: bool = None) -> bool | None:
        """
        Getter/setter for property attribute.

        :param value: whether to wait for animations to complete and match only static (not moving) targets
        :returns: current value if no argument was passed otherwise None
        :raises: :py:class:`ValueError` if value is not boolean or None

        This is useful to handle highly animated environments with lots of moving
        targets where it might be inappropriate to click on a target until it stops
        and the corresponding animation has finished.
        """
        if value is None:
            return self._wait_for_animations
        elif value is True or value is False:
            self._wait_for_animations = value
            return None
        else:
            raise ValueError

    #: whether to wait for animations to complete and match only static (not moving) targets
    wait_for_animations = property(fget=wait_for_animations, fset=wait_for_animations)

    def smooth_mouse_drag(self, value: bool = None) -> bool | None:
        """
        Getter/setter for property attribute.

        :param value: whether to move the mouse cursor to a location instantly or smoothly
        :returns: current value if no argument was passed otherwise None
        :raises: :py:class:`ValueError` if value is not boolean or None

        This is useful if a routine task has to be executed faster without
        supervision or the need of debugging.
        """
        if value is None:
            return self._smooth_mouse_drag
        elif value is True or value is False:
            self._smooth_mouse_drag = value
            return None
        else:
            raise ValueError

    #: whether to move the mouse cursor to a location instantly or smoothly
    smooth_mouse_drag = property(fget=smooth_mouse_drag, fset=smooth_mouse_drag)

    def preprocess_special_chars(self, value: bool = None) -> bool | None:
        """
        Getter/setter for property attribute.

        :param value: whether to preprocess capital and special characters and
                      handle them internally
        :returns: current value if no argument was passed otherwise None

        .. warning:: The characters will be forcefully preprocessed for the
            autopy on linux (capital and special) and vncdotool (capital) backends.
        """
        if value is None:
            return self._preprocess_special_chars
        elif value is True or value is False:
            self._preprocess_special_chars = value
            return None
        else:
            raise ValueError

    #: whether to preprocess capital and special characters and handle them internally
    preprocess_special_chars = property(
        fget=preprocess_special_chars, fset=preprocess_special_chars
    )

    def save_needle_on_error(self, value: bool = None) -> bool | None:
        """
        Getter/setter for property attribute.

        :param value: whether to perform an extra needle dump on matching error
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._save_needle_on_error
        elif value is True or value is False:
            self._save_needle_on_error = value
            return None
        else:
            raise ValueError

    #: whether to perform an extra needle dump on matching error
    save_needle_on_error = property(
        fget=save_needle_on_error, fset=save_needle_on_error
    )

    def image_logging_level(self, value: int = None) -> int | None:
        """
        Getter/setter for property attribute.

        :param value: logging level similar to the python logging module
        :returns: current value if no argument was passed otherwise None

        .. seealso:: See the image logging documentation for more details.
        """
        if value is None:
            return self._image_logging_level
        else:
            self._image_logging_level = value
            return None

    #: logging level similar to the python logging module
    image_logging_level = property(fget=image_logging_level, fset=image_logging_level)

    def image_logging_step_width(self, value: int = None) -> int | None:
        """
        Getter/setter for property attribute.

        :param value: number of digits when enumerating the image
                      logging steps, e.g. value=3 for 001, 002, etc.
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._image_logging_step_width
        else:
            self._image_logging_step_width = value
            return None

    #: number of digits when enumerating the image logging steps, e.g. value=3 for 001, 002, etc.
    image_logging_step_width = property(
        fget=image_logging_step_width, fset=image_logging_step_width
    )

    def image_quality(self, value: int = None) -> int | None:
        """
        Getter/setter for property attribute.

        :param value: quality of the image dumps ranging from 0 for no compression
                      to 9 for maximum compression (used to save space and reduce
                      the disk space needed for image logging)
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._image_quality
        else:
            self._image_quality = value
            return None

    #: quality of the image dumps ranging from 0 for no compression to 9 for maximum compression
    # (used to save space and reduce the disk space needed for image logging)
    image_quality = property(fget=image_quality, fset=image_quality)

    def image_logging_destination(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: relative path of the image logging steps
        :returns: current value if no argument was passed otherwise None
        """
        if value is None:
            return self._image_logging_destination
        else:
            self._image_logging_destination = value
            return None

    #: relative path of the image logging steps
    image_logging_destination = property(
        fget=image_logging_destination, fset=image_logging_destination
    )

    def display_control_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the display control backend
        :returns: current value if no argument was passed otherwise None
        :raises: :py:class:`ValueError` if value is not among the supported backends

        Supported backends:
           * pyautogui - Windows, Linux, and OS X compatible with both the GUI
                         actions and their calls executed on the same machine
           * autopy - Windows, Linux, and OS X compatible with both the GUI
                      actions and their calls executed on the same machine.
           * vncdotool - guest OS independent or Linux remote OS with GUI
                         actions on a remote machine through vnc and their
                         calls on a vnc client machine.
           * xdotool - Linux X server compatible with both the GUI
                       actions and their calls executed on the same machine.
           * qemu - guest OS independent with GUI actions on a virtual machine
                    through Qemu Monitor object (provided by Autotest) and
                    their calls on the host machine.

        .. warning:: To use a particular backend you need to satisfy its dependencies,
            i.e. the backend has to be installed or you will have unsatisfied imports.
        """
        if value is None:
            return self._display_control_backend
        else:
            if value not in ["autopy", "xdotool", "vncdotool", "qemu", "pyautogui"]:
                raise ValueError("Unsupported backend for GUI actions '%s'" % value)
            self._display_control_backend = value
            return None

    #: name of the display control backend
    display_control_backend = property(
        fget=display_control_backend, fset=display_control_backend
    )

    # these methods do not check for valid values since this
    # is already done during region and target initialization
    def find_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the computer vision backend
        :returns: current value if no argument was passed otherwise None

        Supported backends:
            * autopy - simple bitmap matching provided by AutoPy
            * contour - contour matching using overall shape estimation
            * template - template matching using correlation coefficients,
                         square difference, etc.
            * feature - matching using a mixture of feature detection,
                        extraction and matching algorithms
            * cascade - matching using OpenCV pretrained Haar cascades
            * text - text matching using EAST, ERStat, or custom text detection,
                     followed by Tesseract or Hidden Markov Model OCR
            * tempfeat - a mixture of template and feature matching where the
                         first is used as necessary and the second as sufficient stage
            * deep - deep learning matching using convolutional neural network but
                     customizable to any type of deep neural network
            * hybrid - use a composite approach with any of the above methods
                       as matching steps in a fallback sequence

        .. warning:: To use a particular backend you need to satisfy its dependencies,
            i.e. the backend has to be installed or you will have unsatisfied imports.
        """
        if value is None:
            return self._find_backend
        else:
            self._find_backend = value
            return None

    #: name of the computer vision backend
    find_backend = property(fget=find_backend, fset=find_backend)

    def contour_threshold_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the contour threshold backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: normal, adaptive, canny.
        """
        if value is None:
            return self._contour_threshold_backend
        else:
            self._contour_threshold_backend = value
            return None

    #: name of the contour threshold backend
    contour_threshold_backend = property(
        fget=contour_threshold_backend, fset=contour_threshold_backend
    )

    def template_match_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the template matching backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: autopy, sqdiff, ccorr, ccoeff, sqdiff_normed,
        ccorr_normed, ccoeff_normed.
        """
        if value is None:
            return self._template_match_backend
        else:
            self._template_match_backend = value
            return None

    #: name of the template matching backend
    template_match_backend = property(
        fget=template_match_backend, fset=template_match_backend
    )

    def feature_detect_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the feature detection backend
        :returns: current value if no argument was passed otherwise None

        Supported  backends: BruteForce, BruteForce-L1, BruteForce-Hamming,
        BruteForce-Hamming(2), in-house-raw, in-house-region.
        """
        if value is None:
            return self._feature_detect_backend
        else:
            self._feature_detect_backend = value
            return None

    #: name of the feature detection backend
    feature_detect_backend = property(
        fget=feature_detect_backend, fset=feature_detect_backend
    )

    def feature_extract_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the feature extraction backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: ORB, FAST, STAR, GFTT, HARRIS, Dense, oldSURF.
        """
        if value is None:
            return self._feature_extract_backend
        else:
            self._feature_extract_backend = value
            return None

    #: name of the feature extraction backend
    feature_extract_backend = property(
        fget=feature_extract_backend, fset=feature_extract_backend
    )

    def feature_match_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the feature matching backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: ORB, BRIEF, FREAK.
        """
        if value is None:
            return self._feature_match_backend
        else:
            self._feature_match_backend = value
            return None

    #: name of the feature matching backend
    feature_match_backend = property(
        fget=feature_match_backend, fset=feature_match_backend
    )

    def text_detect_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the text detection backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: east, erstat, contours, components.
        """
        if value is None:
            return self._text_detect_backend
        else:
            self._text_detect_backend = value
            return None

    #: name of the text detection backend
    text_detect_backend = property(fget=text_detect_backend, fset=text_detect_backend)

    def text_ocr_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the optical character recognition backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: pytesseract, tesserocr, tesseract (OpenCV), hmm, beamSearch.
        """
        if value is None:
            return self._text_ocr_backend
        else:
            self._text_ocr_backend = value
            return None

    #: name of the optical character recognition backend
    text_ocr_backend = property(fget=text_ocr_backend, fset=text_ocr_backend)

    def deep_learn_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the deep learning backend
        :returns: current value if no argument was passed otherwise None

        Supported backends: pytorch, tensorflow (partial).
        """
        if value is None:
            return self._deep_learn_backend
        else:
            self._deep_learn_backend = value
            return None

    #: name of the deep learning backend
    deep_learn_backend = property(fget=deep_learn_backend, fset=deep_learn_backend)

    def hybrid_match_backend(self, value: str = None) -> str | None:
        """
        Getter/setter for property attribute.

        :param value: name of the hybrid matching backend for unconfigured one-step targets
        :returns: current value if no argument was passed otherwise None

        Supported backends: all nonhybrid backends of :py:func:`GlobalConfig.find_backend`.
        """
        if value is None:
            return self._hybrid_match_backend
        else:
            self._hybrid_match_backend = value
            return None

    #: name of the hybrid matching backend for unconfigured one-step targets
    hybrid_match_backend = property(
        fget=hybrid_match_backend, fset=hybrid_match_backend
    )


class TemporaryConfig(object):
    """
    Proxy a GlobalConfig instance extending it to add context support.

    The context support is such that once this context ends the changes
    to the wrapped config object are restored.

    This is useful when we have a global config instance and need to
    change it only for a few operations.

    ::

        >>> print(GlobalConfig.delay_before_drop)
        0.5
        >>> with TemporaryConfig() as cfg:
        ...     cfg.delay_before_drop = 1.3
        ...     print(cfg.delay_before_drop)
        ...     print(GlobalConfig.delay_before_drop)
        ...
        1.3
        1.3
        >>> print(GlobalConfig.delay_before_drop)
        0.5
    """

    def __init__(self) -> None:
        """Build a temporary global config."""
        object.__setattr__(self, "_original_values", {})

    def __getattribute__(self, name: Any) -> Any:
        """Get attribute given a name."""
        # fallback to GlobalConfig
        return getattr(GlobalConfig, name)

    def __setattr__(self, name: Any, value: Any) -> None:
        """Set attribute given a name and a value."""
        original_values = object.__getattribute__(self, "_original_values")
        # store the original value only at the first set operation,
        # so further changes won't overwrite the history
        if name not in original_values:
            original_values[name] = getattr(GlobalConfig, name)
        setattr(GlobalConfig, name, value)

    def __enter__(self) -> "TemporaryConfig":
        """Set up context manager upon entry."""
        # our temporary config object
        return self

    def __exit__(self, *_: tuple[type, ...]) -> None:
        """Clean up context manager upon exit."""
        original_values = object.__getattribute__(self, "_original_values")
        # restore original configuration values
        for name, value in original_values.items():
            setattr(GlobalConfig, name, value)
        # no need to keep the backup once everything has been restored
        original_values.clear()


class LocalConfig(object):
    """
    Contain locally the configuration of all display control and computer vision backends.

    The local container is reponsible for making them behave according to the selected
    parameters as well as for providing information about them and the current parameters.
    """

    def __init__(self, configure: bool = True, synchronize: bool = True) -> None:
        """
        Build a container for the entire backend configuration.

        :param configure: whether to also generate configuration
        :param synchronize: whether to also apply configuration

        Available algorithms can be seen in the `algorithms` attribute
        whose keys are the algorithm types and values are the members of
        these types. The algorithm types are shortened as `categories`.

        A parameter can be accessed as follows (example)::

            print(self.params["control"]["vnc_hostname"])
        """
        self.categories = {}
        self.algorithms = {}
        self.params = {}

        self.categories["type"] = "backend_types"
        self.algorithms["backend_types"] = ("cv", "dc")

        if configure:
            self.__configure_backend()
        if synchronize:
            self.__synchronize_backend()

    def __configure_backend(
        self, backend: str = None, category: str = "type", reset: bool = False
    ) -> None:
        if category != "type":
            raise UnsupportedBackendError(
                "Backend category '%s' is not supported" % category
            )
        if reset:
            # reset makes no sense here since this is the base configuration
            pass
        if backend is None:
            backend = "cv"
        if backend not in self.algorithms[self.categories[category]]:
            raise UnsupportedBackendError(
                "Backend '%s' is not among the supported ones: "
                "%s" % (backend, self.algorithms[self.categories[category]])
            )

        self.params[category] = {}
        self.params[category]["backend"] = backend

    def configure_backend(
        self, backend: str = None, category: str = "type", reset: bool = False
    ) -> None:
        """
        Generate configuration dictionary for a given backend.

        :param backend: name of a preselected backend, see `algorithms[category]`
        :param category: category for the backend, see `algorithms.keys()`
        :param reset: whether to (re)set all parent configurations as well
        :raises: :py:class:`UnsupportedBackendError` if `backend` is not among
                 the supported backends for the category (and is not `None`) or
                 the category is not found
        """
        self.__configure_backend(backend, category, reset)

    def configure(self, reset: bool = True, **kwargs: dict[str, type]) -> None:
        """
        Generate configuration dictionary for all backends.

        :param reset: whether to (re)set all parent configurations as well

        If multiple categories are available and just some of them are configured,
        the rest will be reset to defaults. To configure specific category without
        changing others, use :py:func:`configure`.
        """
        self.configure_backend(reset=reset)

    def __synchronize_backend(
        self, backend: str = None, category: str = "type", reset: bool = False
    ) -> None:
        if category != "type":
            raise UnsupportedBackendError(
                "Backend category '%s' is not supported" % category
            )
        if reset:
            # reset makes no sense here since this is the base configuration
            pass
        # no backend object to sync to
        backend = "cv" if backend is None else backend
        if backend not in self.algorithms[self.categories[category]]:
            raise UninitializedBackendError(
                "Backend '%s' has not been configured yet" % backend
            )

    def synchronize_backend(
        self, backend: str = None, category: str = "type", reset: bool = False
    ) -> None:
        """
        Synchronize a category backend with the equalizer configuration.

        :param backend: name of a preselected backend, see `algorithms[category]`
        :param category: category for the backend, see `algorithms.keys()`
        :param reset: whether to (re)sync all parent backends as well
        :raises: :py:class:`UnsupportedBackendError` if  the category is not found
        :raises: :py:class:`UninitializedBackendError` if there is no backend object
                 that is configured with and with the required name
        """
        self.__synchronize_backend(backend, category, reset)

    def synchronize(
        self, *args: tuple[type, ...], reset: bool = True, **kwargs: dict[str, type]
    ) -> None:
        """
        Synchronize all backends with the current configuration dictionary.

        :param reset: whether to (re)sync all parent backends as well
        """
        self.synchronize_backend(reset=reset)
