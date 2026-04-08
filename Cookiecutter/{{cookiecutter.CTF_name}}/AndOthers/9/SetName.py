import os
import sys
from pathlib import Path

def main():
    has_error = False

    # 提示用户输入目标名称
    new_name = input("请输入用于重命名的CTF题目名称(name): ").strip()
    if not new_name:
        print("名称不能为空！")
        return

    # 获取当前脚本所在目录作为工作目录（例如 “1” 文件夹）
    current_dir = Path(__file__).resolve().parent

    # 处理 wp 文件夹内部的 wp.md (如果有的话)
    wp_dir = current_dir / "wp"
    if wp_dir.exists():
        wp_md_old = wp_dir / "wp.md"
        wp_md_new = wp_dir / f"{new_name}_wp.md"
        if wp_md_old.exists():
            try:
                # 替换文件内容中的 {name} 为实际输入的名称
                content = wp_md_old.read_text(encoding="utf-8")
                content = content.replace("{name}", new_name)
                wp_md_old.write_text(content, encoding="utf-8")
                # 重命名 wp.md
                wp_md_old.rename(wp_md_new)
                print(f"[成功] 修改并重命名: wp/wp.md -> wp/{new_name}_wp.md")
            except Exception as e:
                print(f"[失败] 处理 wp/wp.md 时出错: {e}")
                has_error = True

    # 定义当前目录下需要重命名的映射关系 {原名称: 新名称}
    items_to_rename = {
        "wp": f"{new_name}_wp",
        "final.py": f"{new_name}_final.py",
        "solve.py": f"{new_name}_solve.py"
    }

    # 1. 遍历并重命名当前目录下的文件和文件夹
    for old_name, target_name in items_to_rename.items():
        old_path = current_dir / old_name
        new_path = current_dir / target_name
        
        if old_path.exists():
            try:
                old_path.rename(new_path)
                print(f"[成功] 找到并重命名: {old_name} -> {target_name}")
            except Exception as e:
                print(f"[失败] 无法重命名 {old_name}: {e}")
                has_error = True
        else:
            print(f"[跳过] 未在当前目录下找到文件或文件夹: {old_name}")

    # 2. 准备重命名当前脚本所在的父文件夹（例如将 "1" 改为 {new_name}）
    parent_dir = current_dir.parent
    new_dir_path = parent_dir / new_name

    # 执行重命名目录前，将当前工作路径切换到上级目录，防止因路径占用报错
    os.chdir(parent_dir)

    try:
        current_dir.rename(new_dir_path)
        print(f"\n[成功] 当前工作文件夹已重命名: {current_dir.name} -> {new_name}")
    except Exception as e:
        print(f"\n[失败] 无法重命名当前文件夹 {current_dir.name}: {e}")
        has_error = True

    # 3. 如果全程没有发生异常，删除脚本自身
    if not has_error:
        try:
            # 目录已经被重命名，脚本的新路径在 new_dir_path 下
            script_path = new_dir_path / Path(__file__).name
            if script_path.exists():
                script_path.unlink()
                print("\n[成功] 所有操作顺利完成，脚本已自动删除。")
        except Exception as e:
            print(f"\n[失败] 脚本自毁失败: {e}")

if __name__ == '__main__':
    main()