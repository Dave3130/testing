# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1llllllll1l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll1l11ll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lllll1lll_opy_
from bstack_utils.helper import bstack1llll1111ll_opy_
import threading
import os
import urllib.parse
class bstack1ll1lll1ll1_opy_(bstack1111111ll1_opy_):
    def __init__(self, bstack1ll1lll111l_opy_):
        super().__init__()
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1llll111_opy_)
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1llll1l1_opy_)
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1ll1lll11ll_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1lll1111_opy_)
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1llll1ll_opy_)
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.QUIT, bstack1llll1ll111_opy_.PRE), self.on_close)
        self.bstack1ll1lll111l_opy_ = bstack1ll1lll111l_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1llll111_opy_(
        self,
        f: bstack1lll1l11ll1_opy_,
        bstack1ll1lll11l1_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤᆺ"):
            return
        if not bstack1llll1111ll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢ࡯ࡥࡺࡴࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᆻ"))
            return
        def wrapped(bstack1ll1lll11l1_opy_, launch, *args, **kwargs):
            response = self.bstack1llllll1lll_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1lll1_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᆼ"): True}).encode(bstack1l1lll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᆽ")))
            if response is not None and response.capabilities:
                if not bstack1llll1111ll_opy_():
                    browser = launch(bstack1ll1lll11l1_opy_)
                    return browser
                bstack1llll1l1l1l_opy_ = json.loads(response.capabilities.decode(bstack1l1lll1_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆾ")))
                if not bstack1llll1l1l1l_opy_: # empty caps bstack1lllll11l11_opy_ bstack111111l111_opy_ bstack1lllllll111_opy_ bstack1lllll1l1l1_opy_ or error in processing
                    return
                bstack1ll1lll1lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1l1l1l_opy_))
                f.bstack1llll1lllll_opy_(instance, bstack1lll1l11ll1_opy_.bstack1lll1ll1ll1_opy_, bstack1ll1lll1lll_opy_)
                f.bstack1llll1lllll_opy_(instance, bstack1lll1l11ll1_opy_.bstack1lll1ll1111_opy_, bstack1llll1l1l1l_opy_)
                browser = bstack1ll1lll11l1_opy_.connect(bstack1ll1lll1lll_opy_)
                return browser
        return wrapped
    def bstack1ll1lll1l1l_opy_(
        self,
        f: bstack1lll1l11ll1_opy_,
        Connection: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤᆿ"):
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡥ࡫ࡶࡴࡦࡺࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇀ"))
            return
        if not bstack1llll1111ll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l1lll1_opy_ (u"ࠩࡳࡥࡷࡧ࡭ࡴࠩᇁ"), {}).get(bstack1l1lll1_opy_ (u"ࠪࡦࡸࡖࡡࡳࡣࡰࡷࠬᇂ")):
                    bstack1ll1lllll1l_opy_ = args[0][bstack1l1lll1_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᇃ")][bstack1l1lll1_opy_ (u"ࠧࡨࡳࡑࡣࡵࡥࡲࡹࠢᇄ")]
                    session_id = bstack1ll1lllll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤᇅ"))
                    f.bstack1llll1lllll_opy_(instance, bstack1lll1l11ll1_opy_.bstack1llll11llll_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥᇆ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1llll1ll_opy_(
        self,
        f: bstack1lll1l11ll1_opy_,
        bstack1ll1lll11l1_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤᇇ"):
            return
        if not bstack1llll1111ll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥࡲࡲࡳ࡫ࡣࡵࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇈ"))
            return
        def wrapped(bstack1ll1lll11l1_opy_, connect, *args, **kwargs):
            response = self.bstack1llllll1lll_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1lll1_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᇉ"): True}).encode(bstack1l1lll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇊ")))
            if response is not None and response.capabilities:
                bstack1llll1l1l1l_opy_ = json.loads(response.capabilities.decode(bstack1l1lll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇋ")))
                if not bstack1llll1l1l1l_opy_:
                    return
                bstack1ll1lll1lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1l1l1l_opy_))
                if bstack1llll1l1l1l_opy_.get(bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᇌ")):
                    browser = bstack1ll1lll11l1_opy_.connect_over_cdp(bstack1ll1lll1lll_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll1lll_opy_
                    return connect(bstack1ll1lll11l1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1llll1l1_opy_(
        self,
        f: bstack1lll1l11ll1_opy_,
        bstack1lll1111l1l_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤᇍ"):
            return
        if not bstack1llll1111ll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡯ࡧࡺࡣࡵࡧࡧࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇎ"))
            return
        def wrapped(bstack1lll1111l1l_opy_, bstack1ll1lllll11_opy_, *args, **kwargs):
            contexts = bstack1lll1111l1l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l1lll1_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢᇏ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lllll11_opy_(bstack1lll1111l1l_opy_)
        return wrapped
    def bstack1llllll1lll_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣᇐ") + str(req) + bstack1l1lll1_opy_ (u"ࠦࠧᇑ"))
        try:
            r = self.bstack1lllll1ll11_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣᇒ") + str(r.success) + bstack1l1lll1_opy_ (u"ࠨࠢᇓ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᇔ") + str(e) + bstack1l1lll1_opy_ (u"ࠣࠤᇕ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lll1111_opy_(
        self,
        f: bstack1lll1l11ll1_opy_,
        Connection: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠤࡢࡷࡪࡴࡤࡠ࡯ࡨࡷࡸࡧࡧࡦࡡࡷࡳࡤࡹࡥࡳࡸࡨࡶࠧᇖ"):
            return
        if not bstack1llll1111ll_opy_():
            return
        def wrapped(Connection, bstack1ll1llll11l_opy_, *args, **kwargs):
            return bstack1ll1llll11l_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l11ll1_opy_,
        bstack1ll1lll11l1_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤᇗ"):
            return
        if not bstack1llll1111ll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡱࡵࡳࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇘ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped