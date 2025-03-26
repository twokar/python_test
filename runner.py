#!/usr/bin/env python3
import os
import subprocess
import time
import sys

def compile_and_run():
    source_file = "/home/src/main.cpp"
    assembly_file = "/home/src/main.s"
    executable_file = "/home/src/app"
    output_file = "/home/src/output.txt"

    # 1. 编译 C++ 代码为汇编文件（可选步骤，便于调试）
    compile_asm_cmd = ["g++", "-S", "-o", assembly_file, source_file]
    try:
        result = subprocess.run(compile_asm_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        error_msg = f"汇编编译失败:\n{e.stderr or e.stdout}"
        with open(output_file, "w") as f:
            f.write(error_msg)
        sys.exit(1)  # 退出容器，并返回错误信息

    # 2. 编译生成可执行文件
    compile_exec_cmd = ["g++", "-o", executable_file, source_file]
    try:
        result = subprocess.run(compile_exec_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        error_msg = f"编译失败:\n{e.stderr or e.stdout}"
        with open(output_file, "w") as f:
            f.write(error_msg)
        sys.exit(1)

    # 3. 运行可执行文件，并记录执行时间
    try:
        start_time = time.time()
        run_result = subprocess.run([executable_file], check=True, capture_output=True, text=True)
        exec_time = time.time() - start_time

        # 拼接输出结果及执行时间信息
        output = run_result.stdout.strip() + "\n"
        output += f"Execution Time: {exec_time:.6f} seconds\n"
        with open(output_file, "w") as f:
            f.write(output)
    except subprocess.CalledProcessError as e:
        error_msg = f"程序运行失败:\n{e.stderr or e.stdout}"
        with open(output_file, "w") as f:
            f.write(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    compile_and_run()
