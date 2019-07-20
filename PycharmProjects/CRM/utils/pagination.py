# -*- coding: utf-8 -*-
# @Time : 2019/6/22 9:37
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : pagination.py
# @Software: PyCharm
from django.utils.safestring import mark_safe
from copy import deepcopy


class Pagination:
    """
    分页器
    """

    def __init__(self, request, all_count, per_number=10, max_show=11):
        # 基本的 url
        self.base_url = request.path_info
        self.all_count = all_count
        self.per_number = per_number
        # 分页保留搜索条件
        # 我们尽量不要波及源码，所以做个深拷贝
        self.query_params = deepcopy(request.GET)
        # request.GET——默认不许修改 ._mutable=True——就可以修改了
        self.query_params._mutable = True
        # 最多显示的页码数
        self.max_show = max_show
        self.half_show = max_show // 2
        # 获取当前页码
        try:
            self.current_page = int(request.GET.get('page', default=1))
            if self.current_page < 1:
                self.current_page = 1
            elif self.current_page > self.total_number:
                self.current_page = self.total_number
        except Exception as e:
            self.current_page = 1
        # 1总页码数大于显示数
        if self.total_number <= self.max_show:
            self.page_start = 1
            self.page_end = self.total_number
        else:
            if self.current_page <= self.half_show:
                self.page_start = 1
                self.page_end = self.max_show
            elif self.current_page + self.half_show >= self.total_number:
                self.page_start = self.total_number - self.max_show + 1
                self.page_end = self.total_number
            else:
                # 2最多显示11个
                self.page_start = self.current_page - self.half_show
                self.page_end = self.current_page + self.half_show

    @property
    def total_number(self):
        # 总也码数 = 总数据量 / 每页显示
        total_number, more = divmod(self.all_count, self.per_number)
        # 如果有余数，就加一
        if more:
            total_number += 1
        return total_number

    # 显示页码数
    # @property
    # def show_page_range(self):
    #     # 1总页码数大于显示数
    #     if self.total_number <= self.max_show:
    #         page_start, page_end = 1, self.total_number
    #     else:
    #         if self.current_page <= self.half_show:
    #             page_start = 1
    #             page_end = self.max_show
    #         elif self.current_page + self.half_show >= self.total_number:
    #             page_start = self.total_number - self.max_show + 1
    #             page_end = self.total_number
    #         else:
    #             # 2最多显示11个
    #             page_start = self.current_page - self.half_show
    #             page_end = self.current_page + self.half_show
    #     return range(page_start, page_end + 1)

    # 显示页码数
    @property
    def show_page_range(self):
        # 1总页码数大于显示数
        if self.total_number <= self.max_show:
            return range(self.page_start, self.page_end + 1)
        else:
            if self.current_page <= self.half_show:
                self.page_end = self.max_show
            elif self.current_page + self.half_show >= self.total_number:
                self.page_start = self.total_number - self.max_show + 1
            else:
                # 2最多显示11个
                self.page_start = self.current_page - self.half_show
                self.page_end = self.current_page + self.half_show
            return range(self.page_start, self.page_end + 1)

    # 分页起始值
    @property
    def start(self):
        return (self.current_page - 1) * self.per_number

    # 分页结束值
    @property
    def end(self):
        return self.current_page * self.per_number

    @property
    def show_li(self):
        # 存放li标签的列表
        html_list = []
        # request.GET 是个 QueryDict，把 {'page': 1} 添加在 QueryDict 里
        self.query_params['page'] = 1
        # request.GET.urlencode()——编码成 url
        first_li = '<li><a href="{}?{}">首页</a></li>'.format(self.base_url, self.query_params.urlencode())
        html_list.append(first_li)

        if self.current_page == 1:
            prev_li = '<li class="disabled"><a><<</a></li>'
        else:
            self.query_params['page'] = self.current_page - 1
            prev_li = '<li><a href="{0}?{1}"><<</a></li>'.format(self.base_url, self.query_params.urlencode())
        html_list.append(prev_li)

        for num in range(self.page_start, self.page_end + 1):
            self.query_params['page'] = num
            if self.current_page == num:
                li_html = '<li class="active"><a href="{0}?{1}">{2}</a></li>'.format(self.base_url,
                                                                                     self.query_params.urlencode(), num)
            else:
                li_html = '<li><a href="{0}?{1}">{2}</a></li>'.format(self.base_url,
                                                                      self.query_params.urlencode(), num)
            html_list.append(li_html)

        if self.current_page == self.total_number:
            next_li = '<li class="disabled"><a>>></a></li>'
        else:
            self.query_params['page'] = self.current_page + 1
            next_li = '<li><a href="{0}?{1}">>></a></li>'.format(self.base_url, self.query_params.urlencode())

        html_list.append(next_li)

        self.query_params['page'] = self.total_number
        last_li = '<li><a href="{0}?{1}">尾页</a></li>'.format(self.base_url, self.query_params.urlencode())
        html_list.append(last_li)

        return mark_safe(''.join(html_list))
