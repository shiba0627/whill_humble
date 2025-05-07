# whill_ros2-humble_ubuntu22.04
## 1. WHILLの電動車いす制御
[WHILL Model C](https://whill.inc/jp/model-c)

[ros2ドキュメント](https://docs.ros.org/en/humble/index.html)
## 2. 動作環境
| ソフトウェア・使用機器 | バージョン |
| -------------------- | ---------- |
| 制御用PC(PC2)         | Ubuntu 22.04 LTS  |
| ROS2                 | Humble     |
| 走行司令送信PC(PC1)    |Windows10|
| 電動車いす             | WHILL model CR   |
## 3. ディレクトリ構成
```
.
├── build
├── install
├── log 
├── memo.md
├── README.md
└── src
    ├── build
    ├── install
    ├── log
    ├── ros2_whill
    ├── ros2_whill_interfaces
    └── urg_node2
```
## 4. コマンド
### ros2インストール
```bash
locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # 変更されたか確認

sudo apt install software-properties-common
sudo add-apt-repository universe

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt install ros-humble-desktop
sudo apt install ros-humble-ros-base
sudo apt install ros-dev-tools

source /opt/ros/humble/setup.bash    #ターミナル起動のたび、毎回唱える呪文
```
### コンパイルなど
```bash
source install/local_setup.bash
colcon build --cmake-args '-DCMAKE_BUILD_TYPE=Release'#ビルド最適化モードでビルド
```
### パッケージインストール
```bash
sudo apt install git
sudo apt install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub//公開鍵をコピー

cd whill_ros2-humble_ubuntu22.04
mkdir src
rosdep install -i --from-path src --rosdistro humble -y
colcon build --cmake-args '-DCMAKE_BUILD_TYPE=Release'
```
### ソース設定
```bash
#bashrcに書いておくと便利
cat ~/.bashrc#確認
vim ~/.bashrc#編集
source install/setup.bash
source install/local_setup.bash
source /opt/ros/humble/setup.bash    #ターミナル起動のたび、毎回唱える呪文
```
### ノード起動
```bash
ros2 run ros2_whill whill_modelc_publisher
ros2 run ros2_whill whill_modelc_controller
ros2 topic list
```
### その他
```bash
#ディレクトリ構造を表示
tree -L 2 #階層指定2
#シリアルポートアクセス許可
sudo usermod -a -G dialout $USER
```
