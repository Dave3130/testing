# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import (
    bstack1llllll111l_opy_,
    bstack1llll1l111l_opy_,
    bstack1llllll1l1l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l1ll11_opy_ import bstack1llll111l11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lll1111l1_opy_
from bstack_utils.helper import bstack1lll1ll111l_opy_
import threading
import os
import urllib.parse
class bstack1ll1lll111l_opy_(bstack1llll1llll1_opy_):
    def __init__(self, bstack1ll1ll1llll_opy_):
        super().__init__()
        bstack1llll111l11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllll1ll11_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1ll1ll1ll1l_opy_)
        bstack1llll111l11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllll1ll11_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1ll1ll1l1l1_opy_)
        bstack1llll111l11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1ll1lll1l11_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1ll1lll1ll1_opy_)
        bstack1llll111l11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllllll111_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1ll1ll1ll11_opy_)
        bstack1llll111l11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllll1ll11_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1ll1ll1lll1_opy_)
        bstack1llll111l11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.QUIT, bstack1llll1l111l_opy_.PRE), self.on_close)
        self.bstack1ll1ll1llll_opy_ = bstack1ll1ll1llll_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1ll1ll1l_opy_(
        self,
        f: bstack1llll111l11_opy_,
        bstack1ll1lll1111_opy_: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠢ࡭ࡣࡸࡲࡨ࡮ࠢᇔ"):
            return
        if not bstack1lll1ll111l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡭ࡣࡸࡲࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇕ"))
            return
        def wrapped(bstack1ll1lll1111_opy_, launch, *args, **kwargs):
            response = self.bstack11111111ll_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇖ"): True}).encode(bstack1l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇗ")))
            if response is not None and response.capabilities:
                if not bstack1lll1ll111l_opy_():
                    browser = launch(bstack1ll1lll1111_opy_)
                    return browser
                bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack1l1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇘ")))
                if not bstack1lllll11111_opy_: # empty caps bstack1lllll1ll1l_opy_ bstack1lllll1l1ll_opy_ bstack1llll1l1111_opy_ bstack1llll1ll111_opy_ or error in processing
                    return
                bstack1ll1lll11l1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllll11111_opy_))
                f.bstack1llll1l1lll_opy_(instance, bstack1llll111l11_opy_.bstack1lll1l1l11l_opy_, bstack1ll1lll11l1_opy_)
                f.bstack1llll1l1lll_opy_(instance, bstack1llll111l11_opy_.bstack1lll11lll11_opy_, bstack1lllll11111_opy_)
                browser = bstack1ll1lll1111_opy_.connect(bstack1ll1lll11l1_opy_)
                return browser
        return wrapped
    def bstack1ll1lll1ll1_opy_(
        self,
        f: bstack1llll111l11_opy_,
        Connection: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢᇙ"):
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇚ"))
            return
        if not bstack1lll1ll111l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡲࡹࠧᇛ"), {}).get(bstack1l1_opy_ (u"ࠨࡤࡶࡔࡦࡸࡡ࡮ࡵࠪᇜ")):
                    bstack1ll1ll1l1ll_opy_ = args[0][bstack1l1_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᇝ")][bstack1l1_opy_ (u"ࠥࡦࡸࡖࡡࡳࡣࡰࡷࠧᇞ")]
                    session_id = bstack1ll1ll1l1ll_opy_.get(bstack1l1_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡎࡪࠢᇟ"))
                    f.bstack1llll1l1lll_opy_(instance, bstack1llll111l11_opy_.bstack1lll11ll11l_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࠣᇠ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1ll1lll1_opy_(
        self,
        f: bstack1llll111l11_opy_,
        bstack1ll1lll1111_opy_: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢᇡ"):
            return
        if not bstack1lll1ll111l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡣࡰࡰࡱࡩࡨࡺࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇢ"))
            return
        def wrapped(bstack1ll1lll1111_opy_, connect, *args, **kwargs):
            response = self.bstack11111111ll_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇣ"): True}).encode(bstack1l1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇤ")))
            if response is not None and response.capabilities:
                bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack1l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇥ")))
                if not bstack1lllll11111_opy_:
                    return
                bstack1ll1lll11l1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllll11111_opy_))
                if bstack1lllll11111_opy_.get(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᇦ")):
                    browser = bstack1ll1lll1111_opy_.connect_over_cdp(bstack1ll1lll11l1_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll11l1_opy_
                    return connect(bstack1ll1lll1111_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1ll1l1l1_opy_(
        self,
        f: bstack1llll111l11_opy_,
        bstack1lll11111l1_opy_: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᇧ"):
            return
        if not bstack1lll1ll111l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡴࡥࡸࡡࡳࡥ࡬࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇨ"))
            return
        def wrapped(bstack1lll11111l1_opy_, bstack1ll1lll1l1l_opy_, *args, **kwargs):
            contexts = bstack1lll11111l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l1_opy_ (u"ࠢࡢࡤࡲࡹࡹࡀࡢ࡭ࡣࡱ࡯ࠧᇩ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lll1l1l_opy_(bstack1lll11111l1_opy_)
        return wrapped
    def bstack11111111ll_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨᇪ") + str(req) + bstack1l1_opy_ (u"ࠤࠥᇫ"))
        try:
            r = self.bstack1llll1l11ll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨᇬ") + str(r.success) + bstack1l1_opy_ (u"ࠦࠧᇭ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᇮ") + str(e) + bstack1l1_opy_ (u"ࠨࠢᇯ"))
            traceback.print_exc()
            raise e
    def bstack1ll1ll1ll11_opy_(
        self,
        f: bstack1llll111l11_opy_,
        Connection: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠢࡠࡵࡨࡲࡩࡥ࡭ࡦࡵࡶࡥ࡬࡫࡟ࡵࡱࡢࡷࡪࡸࡶࡦࡴࠥᇰ"):
            return
        if not bstack1lll1ll111l_opy_():
            return
        def wrapped(Connection, bstack1ll1lll1lll_opy_, *args, **kwargs):
            return bstack1ll1lll1lll_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1llll111l11_opy_,
        bstack1ll1lll1111_opy_: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢᇱ"):
            return
        if not bstack1lll1ll111l_opy_():
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥ࡯ࡳࡸ࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇲ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped