#/joyを購読し、走行履歴を作成・保存するノードをつくりたいが、今はパブリッシャ練習コード
import rclpy
from rclpy.node import Node

from std_msgs.msg import String#トピックの型


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')#ノード名
        self.publisher_ = self.create_publisher(String, 'topic', 10)#キューサイズ10の'topic'をパブリッシュ
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)#コールバックタイマ, 0.5s毎にtimer_callbackを呼ぶ
        self.i = 0#コールバックカウンタ

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)#パブリッシュ
        self.get_logger().info('Publishing: "%s"' % msg.data)#コマンドラインに出力
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()#ノードをインスタンス化

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()