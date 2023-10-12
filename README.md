```
Cách sử dụng code socket giao tiếp từ máy tính -> Jetson -> Arduino (Phải kết nối cùng 1 model wifi)
```

> Server_Jetson được cài trên Jetson nano có nhiệm vụ gửi tín hiệu nhận được từ Client sang Arduino(điều khiển xe)

Cách khởi chạy

> python server_Jetson.py --host localhost --port 9999  --ip_cam ip_camera --com com_arduino

> python client_COM.py --host ip_server(Jetson) --port 9999

> Check cổng com trên jetson nano

> ls /dev/
>
> Thông thường cổng COM kết nối vs arduino sẽ tên là /dev/ttyACM0
