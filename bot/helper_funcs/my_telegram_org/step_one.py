#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" STEP ONE """

from aiohttp import ClientSession
from json import loads


async def request_tg_code_get_random_hash(input_phone_number: str) -> str:
    """ requests Login Code
    and returns a random_hash
    which is used in STEP TWO """
    request_url = "https://my.telegram.org/auth/send_password"
    request_data = {
        "phone": input_phone_number
    }
    async with ClientSession() as requests:
        response_c = await requests.post(request_url, data=request_data)
        json_response = loads(await response_c.text())
    return json_response["random_hash"]
