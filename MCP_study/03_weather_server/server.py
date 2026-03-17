#!/usr/bin/env python3
"""
天气查询 MCP Server
使用 Open-Meteo API（免费，无需 API Key）

使用方法:
    python server.py

示例调用:
    北京：get_weather("北京", 39.9042, 116.4074)
    上海：get_weather("上海", 31.2304, 121.4737)
    广州：get_weather("广州", 23.1291, 113.2644)
"""

from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Weather")

# 常见城市坐标
CITIES = {
    "北京": (39.9042, 116.4074),
    "上海": (31.2304, 121.4737),
    "广州": (23.1291, 113.2644),
    "深圳": (22.5431, 114.0579),
    "杭州": (30.2741, 120.1551),
    "成都": (30.5728, 104.0668),
    "武汉": (30.5928, 114.3055),
    "西安": (34.3416, 108.9398),
}

@mcp.tool()
def get_weather(city: str, latitude: float, longitude: float) -> str:
    """
    获取指定城市的当前天气
    
    Args:
        city: 城市名称
        latitude: 纬度
        longitude: 经度
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    weather = data.get("current_weather", {})
    
    return f"""
📍 {city} 当前天气
━━━━━━━━━━━━━━━━
🌡️  温度：{weather.get('temperature', 'N/A')}°C
💨 风速：{weather.get('windspeed', 'N/A')} km/h
🧭 风向：{weather.get('winddirection', 'N/A')}°
☁️  天气代码：{weather.get('weathercode', 'N/A')}
━━━━━━━━━━━━━━━━
    """.strip()


@mcp.tool()
def get_weather_by_city_name(city_name: str) -> str:
    """
    通过城市名称获取天气（自动查找坐标）
    
    支持的城市：北京、上海、广州、深圳、杭州、成都、武汉、西安
    
    Args:
        city_name: 城市名称
    """
    if city_name not in CITIES:
        return f"错误：不支持的城市 '{city_name}'\n支持的城市：{', '.join(CITIES.keys())}"
    
    lat, lon = CITIES[city_name]
    return get_weather(city_name, lat, lon)


if __name__ == "__main__":
    mcp.run()
