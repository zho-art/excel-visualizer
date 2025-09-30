class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error_prev = 0
        self.error_sum = 0

    def update(self, error):
        self.error_sum += error
        delta_error = error - self.error_prev
        self.error_prev = error
        return self.kp * error + self.ki * self.error_sum + self.kd * delta_error

def calculate_pid_params(center_x, center_y, img_w, img_h):
    # 这里可以根据center_x和center_y来计算PID参数，以下为示例
    kp = 0.1
    ki = 0.01
    kd = 0.05
    return PIDController(kp, ki, kd)

def adjust_robot_position(offset_x, offset_y, img_w, img_h):
    # 计算目标中心点
    center_x = img_w / 2
    center_y = img_h / 2
    
    # 创建PID控制器
    pid = calculate_pid_params(center_x, center_y, img_w, img_h)
    
    # 计算误差
    error_x = center_x - offset_x
    error_y = center_y - offset_y
    
    # 更新PID控制器
    output_x = pid.update(error_x)
    output_y = pid.update(error_y)
    
    # 根据PID输出调整机器人位置，这里只是示例，具体实现需要根据机器人的API
    print(f"Adjusting robot position: x={output_x}, y={output_y}")
    # 假设这里有代码来实际移动机器人

def adjust_eye_position(offset_x, offset_y, img_w, img_h):
    # 创建PID控制器
    pid = calculate_pid_params(img_w / 2, img_h / 2, img_w, img_h)
    
    # 计算误差
    error_x = img_w / 2 - offset_x
    error_y = img_h / 2 - offset_y
    
    # 更新PID控制器
    output_x = pid.update(error_x)
    output_y = pid.update(error_y)
    
    # 根据PID输出调整LED眼睛位置，这里只是示例，具体实现需要根据LED眼睛的控制接口
    print(f"Adjusting eye position: x={output_x}, y={output_y}")
    # 假设这里有代码来实际调整LED眼睛的位置

# 示例调用
adjust_robot_position(100, 150, 640, 480)
adjust_eye_position(100, 150, 640, 480)