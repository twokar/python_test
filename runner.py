#!/usr/bin/env python3
import subprocess
import time
import sys

def compile_and_run():
    source_file = "/home/src/main.cpp"
    assembly_file = "/home/src/main.s"
    executable_file = "/home/src/app"

    # 1. 编译 C++ 代码为汇编文件（可选步骤）
    compile_asm_cmd = ["g++", "-S", "-o", assembly_file, source_file]
    try:
        result_asm = subprocess.run(compile_asm_cmd, check=True, capture_output=True, text=True)
        if result_asm.stdout:
            print(result_asm.stdout)
        if result_asm.stderr:
            print(result_asm.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        error_msg = "汇编编译失败:\n" + (e.stderr if e.stderr else e.stdout)
        print(error_msg, file=sys.stderr)
        sys.exit(1)

    # 2. 编译生成可执行文件
    compile_exec_cmd = ["g++", "-o", executable_file, source_file]
    try:
        result_exec = subprocess.run(compile_exec_cmd, check=True, capture_output=True, text=True)
        if result_exec.stdout:
            print(result_exec.stdout)
        if result_exec.stderr:
            print(result_exec.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        error_msg = "编译失败:\n" + (e.stderr if e.stderr else e.stdout)
        print(error_msg, file=sys.stderr)
        sys.exit(1)

    # 3. 运行可执行文件，并记录执行时间
    try:
        start_time = time.time()
        run_result = subprocess.run([executable_file], check=True, capture_output=True, text=True)
        exec_time = time.time() - start_time

        output = run_result.stdout.strip()
        # 输出程序运行结果
        print(output)
        # 输出执行时间
        print("Execution Time: {:.6f}".format(exec_time))
    except subprocess.CalledProcessError as e:
        error_msg = "程序运行失败:\n" + (e.stderr if e.stderr else e.stdout)
        print(error_msg, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    compile_and_run()
