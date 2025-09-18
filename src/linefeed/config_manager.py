from .api_config import ApiConfig
from .device_config import DeviceConfig
from .format_config import FormatConfig
from pydantic import BaseModel


class ConfigFile(BaseModel):
    device: DeviceConfig
    format: FormatConfig
    api: ApiConfig


class ConfigManager:
    def __init__(self, config_path: str = "config.yaml"):
        self._config_path = config_path
        self._config_file: ConfigFile = self._load_config_file(self._config_path)

    @classmethod
    def _load_config_file(cls, path: str = "config.yaml") -> ConfigFile:
        """
        Loads the configuration file from the specified path.

        Parameters
        ----------
        path : str, optional
            The path to the configuration file, by default "config.yaml".

        Returns
        -------
        ConfigFile
            The loaded configuration as a ConfigFile object.

        Raises
        ------
        FileNotFoundError
            If the configuration file does not exist at the specified path.
        ValueError
            If the configuration file is malformed or cannot be parsed.
        """
        import yaml

        try:
            with open(path, "r", encoding="utf-8") as f:
                config_data = yaml.safe_load(f)
            return ConfigFile(**config_data)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Configuration file not found: {path}") from e
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing configuration file: {str(e)}") from e

    @property
    def device_config(self) -> DeviceConfig:
        return self._config_file.device

    @property
    def format_config(self) -> FormatConfig:
        return self._config_file.format

    @property
    def api_config(self) -> ApiConfig:
        return self._config_file.api
