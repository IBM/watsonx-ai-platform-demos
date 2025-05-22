import shutil
import subprocess
import tomllib
from pathlib import Path
import os
import shutil
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
# Replace before deploy
env_path = "/Users/thomassuedbroecker/Documents/tsuedbro/dev/watsonx-ai-platform-demos/workshops/regional_techXchange_2025_05/03_phase3_agents/agents/langgraph_implementation/src/langgraph_react_agent"
env_dest_name = "langgraph_react_agent_custom-0.1.4"
def get_package_name_and_version(pyproject_path: str) -> tuple[str, str]:
    """
    Parse pyproject.toml to get the package name and version.

    :param pyproject_path: Path to pyproject.toml
    :type pyproject_path: str
    """
    logging.debug(f"***Log build: Parse pyproject.toml to get the package name and version.")
    with open(pyproject_path, "rb") as f:
        pyproject_data = tomllib.load(f)
    tool_poetry = pyproject_data.get("tool", {}).get("poetry", {})
    package_name = tool_poetry.get("name")
    package_version = tool_poetry.get("version")
    if not package_name or not package_version:
        raise ValueError("Package name or version is missing in pyproject.toml.")
    return package_name, package_version


def build_zip_sc(sc_dir: Path) -> None:
    """
    Build and package a source distribution as a ZIP archive.

    This function performs the following steps:
    1. Builds a source distribution using Poetry.
    2. Extracts the built archive.
    3. Normalizes file timestamps to fix ZIP timestamp issues.
    4. Creates a ZIP archive of the source directory.

    :param sc_dir: Path to the source directory for building and packaging.
    :type sc_dir: Path
    """

    logging.debug(f"***Log build: 1. Builds a source distribution using Poetry.")
    subprocess.run(["poetry", "build", f"--output={sc_dir.parent}", "--format=sdist"], check=True)
    logging.debug(f"***Log build: 2. Extract the build archive.")
    shutil.unpack_archive(sc_dir.with_suffix(".tar.gz"), sc_dir.parent)

    logging.debug(f"***Log build: 3. Normalizes file timestamps to fix ZIP timestamp issues.")
    for file in sc_dir.parent.rglob("*"):
        print(f"***Log build zip package: {file.name}")
        if file.is_file():
            if ".env_template" in file.name:
                logging.debug(f"***Log build zip package: File will not be added '.env_template'")
                try: 
                    os.remove(file)
                    print(f"File '{file}' deleted successfully.")
                except FileNotFoundError: 
                        print(f"File '{file}' not found.")
            else:
                file.touch()

    # Replace
    logging.debug(f"***Log build: 3.1 Add '.env' file to zip folder.")    
    source_env_file=f"{env_path}/.env"
    logging.debug(f"***Log build: dest path {sc_dir.parent}") 
    dest_env_file= f"{sc_dir.parent}/{env_dest_name}/src/langgraph_react_agent/.env"
    shutil.copyfile(source_env_file, dest_env_file)
    
    logging.debug(f"***Log build: 4. Create a ZIP archive of the source directory.")
    zip_dir = str(sc_dir.with_suffix(""))
    shutil.make_archive(zip_dir, "zip", zip_dir)


if __name__ == "__main__":
    pkg_name, pkg_version = get_package_name_and_version("../pyproject.toml")
    pkg_ext_sc = Path(__file__).parent / ".." / "dist" / f"{pkg_name.replace('-', '_')}-{pkg_version}.zip"
    build_zip_sc(pkg_ext_sc)
