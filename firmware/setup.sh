if [ ! -d "esp" ]; then
    mkdir esp
    cd esp
    
    git clone --recursive https://github.com/espressif/esp-idf.git
    
    cd esp-idf
    ./install.sh esp32s2

    export IDF_GITHUB_ASSETS="dl.espressif.com/github_assets"
    ./install.sh

    source ./export.sh
fi
