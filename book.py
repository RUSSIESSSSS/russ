#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/19 22:09
# @Author  : pauline
# @File    : book.py


#
# books = [{"bid": 1, "name": "book_name_1", "price": 1.0, "summary": "这是sid=1这本书的简介字段"},
#          {"bid": 2, "name": "book_name_2",
#           "price": 2.0,
#           "summary": "这是sid=2这本书的简介字段"}]  # 一本书用字典存储，多本书用一个列表存储


books = []


def menu():
    """打印所有可以输入的序号"""
    print("*****************************")
    print("*      图书管理系统           *")
    print("* 1. 添加新图书信息           *")
    print("* 2. 通过图书ID修改图书信息      *")
    print("* 3. 通过图书ID删除图书信息      *")
    print("* 4. 通过书名删除图书信息      *")
    print("* 5. 通过图书ID查询图书信息      *")
    print("* 6. 通过书名查询图书信息      *")
    print("* 7. 显示所有图书信息         *")
    print("* 8. 退出系统                *")
    print("*****************************")
    select_op = input("请输入1-8中你想要的数字")
    return select_op


def get_book_by_book_id(book_id):
    """参数为图书ID
    如果图书存在，则输出图书信息，不存在输出提示
    返回是否查询成功"""
    for book in books:
        if book['book_id'] == book_id:
            print(f"图书{book_id}存在")
            return "查询成功"
        else:
            print(f"图书{book_id}不存在")
            return "查询失败"


def get_book_by_book_name(book_name):
    """
    获取book信息，通过book_name
    """
    for book in books:
        if book['book_name'] == book_name:
            print(f"当前书籍{book_name}存在")
            return "通过book_name查询成功"
        else:
            print(f"当前书籍{book_name}不存在")
            return "通过book_name查询失败"


def delete_book_by_book_name(book_name):
    """参数为书名
    如果图书存在，则进行删除（同名图书全部删除），不存在输出提示
    返回是否删除成功"""
    del_data = []
    for book in books:
        if book['book_name'] == book_name:
            del_data.append(book)

    if len(del_data) > 0:
        for d in del_data:
            books.remove(d)
            print(f"图书名称为 {d['book_name']} 的图书删除成功")
        else:
            print(f"成功删除{len(del_data)}本图书")
            return "删除成功"
    else:
        print("图书id不存在，无法删除")
        return "删除失败"


def update_book_by_book_id(book_id):
    """
    参数为图书ID
    如果图书存在，则进行修改，不存在输出提示
    返回是否修改成功
    """
    for book in books:
        if book['book_id'] == book_id:
            print("书籍存在，可以修改")
            book_name = get_book_name()
            book_price = get_book_price()
            book_summary = get_book_summary()
            book['book_name'] = book_name
            book['book_summary'] = book_summary
            book['book_price'] = book_price
            print("修改成功")
            return "书籍信息修改成功"
    else:
        print(f"没有{book_id}对应的图书信息")
        return "修改失败"


def get_book_id():
    """输入编号并返回（字符串类型）eg. s01"""
    book_id = input("请输入图书编号： ")
    print("book_id ==", book_id)
    return str(book_id)


def get_book_name():
    """输入书名并返回（字符串类型)"""
    book_name = input("请输入图书书名： ")
    print("图书名称 == ", book_name)
    return str(book_name)


def get_book_price():
    """输入价格并返回（整型)"""
    book_price = input("请输入图书价格： ")
    if book_price.isdigit():
        print("图书价格 == ", book_price)
        return book_price
    else:
        print("请输入一个整数价格")


def get_book_summary():
    """输入简介并返回（字符串类型）"""
    book_summary = input("请输入图书简介 ： ")
    print("图书简介== ", book_summary)
    return book_summary


def add_books(book_id, book_name, book_price, book_summary):
    """添加一本书"""
    for book in books:
        if book["book_id"] == book_id:
            print(f"已经存在相同的{book_id}的书籍")
            return "******添加失败******"
    else:
        # book = {"sid": sid, "name": name, "price": price, "summary": summary}
        book = {"book_id": book_id, "book_name": book_name, "book_price": book_price, "book_summary": book_summary}
        books.append(book)
        return "添加图书成功！！"


def delete_book_by_book_id(book_id):
    """通过book_id删除书"""
    for book in books:
        if book['book_id'] == book_id:
            books.remove(book)
            print("删除成功")
            return "删除成功"

    else:
        print(f"没有{book_id}对应的书籍信息")
        return "删除失败"


def show_all_books():
    """查询所有的书"""
    print("所有图书信息如下： ")
    for book in books:
        print(book)


def book_manager():
    """
    对用户输入内容进行输入校验
    根据用户输入内容选择不同功能执行
    """
    print("*******请查看如下选项，并输入你想执行的序号******* ")
    while True:
        select_id = menu()
        if len(select_id) == 1 and select_id in "12345678":
            if select_id == '1':
                book_id = get_book_id()
                book_name = get_book_name()
                book_price = get_book_price()
                book_summary = get_book_summary()
                add_books(book_id=book_id, book_name=book_name, book_price=book_price, book_summary=book_summary)
                print("图书添加成功")
                print("这是目前所有的书籍:", books)
            elif select_id == '2':
                book_id = get_book_id()
                update_book_by_book_id(book_id)
            elif select_id == '3':
                book_id = get_book_id()
                delete_book_by_book_id(book_id=book_id)
            elif select_id == '4':
                book_name = get_book_name()
                delete_book_by_book_name(book_name=book_name)

            elif select_id == '5':
                book_id = get_book_id()
                get_book_by_book_id(book_id)
            elif select_id == '6':
                book_name = get_book_name()
                get_book_by_book_name(book_name)
            elif select_id == '7':
                show_all_books()
            else:
                print("没有可执行的内容")
                break


if __name__ == '__main__':
    book_manager()
