# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lllllll11l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1lll111_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll111111_opy_
from bstack_utils.helper import bstack1lll11l1lll_opy_
import threading
import os
import urllib.parse
class bstack1ll1lll11l1_opy_(bstack1lllllll1l1_opy_):
    def __init__(self, bstack1ll1lll111l_opy_):
        super().__init__()
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1l1ll1_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1ll1l1l1_opy_)
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1l1ll1_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1ll1llll_opy_)
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1ll1ll1ll1l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1ll1l111_opy_)
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1l1ll1_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1lll1l11_opy_)
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.QUIT, bstack1llll1lllll_opy_.PRE), self.on_close)
        self.bstack1ll1lll111l_opy_ = bstack1ll1lll111l_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1ll1l1l1_opy_(
        self,
        f: bstack1lll1lll111_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠦࡱࡧࡵ࡯ࡥ࡫ࠦᇘ"):
            return
        if not bstack1lll11l1lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡱࡧࡵ࡯ࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇙ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, launch, *args, **kwargs):
            response = self.bstack1llll1l11l1_opy_(f.platform_index, instance.ref(), json.dumps({bstack1lll11l_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᇚ"): True}).encode(bstack1lll11l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᇛ")))
            if response is not None and response.capabilities:
                if not bstack1lll11l1lll_opy_():
                    browser = launch(bstack1ll1ll1lll1_opy_)
                    return browser
                bstack1llll1lll11_opy_ = json.loads(response.capabilities.decode(bstack1lll11l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇜ")))
                if not bstack1llll1lll11_opy_: # empty caps bstack111111111l_opy_ bstack1lllll111l1_opy_ bstack1llll11l1ll_opy_ bstack1lllll11ll1_opy_ or error in processing
                    return
                bstack1ll1ll1l1ll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1lll11_opy_))
                f.bstack1llll1ll11l_opy_(instance, bstack1lll1lll111_opy_.bstack1llll111lll_opy_, bstack1ll1ll1l1ll_opy_)
                f.bstack1llll1ll11l_opy_(instance, bstack1lll1lll111_opy_.bstack1lll1llll1l_opy_, bstack1llll1lll11_opy_)
                browser = bstack1ll1ll1lll1_opy_.connect(bstack1ll1ll1l1ll_opy_)
                return browser
        return wrapped
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1lll1lll111_opy_,
        Connection: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠤࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠦᇝ"):
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇞ"))
            return
        if not bstack1lll11l1lll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1lll11l_opy_ (u"ࠫࡵࡧࡲࡢ࡯ࡶࠫᇟ"), {}).get(bstack1lll11l_opy_ (u"ࠬࡨࡳࡑࡣࡵࡥࡲࡹࠧᇠ")):
                    bstack1ll1ll11lll_opy_ = args[0][bstack1lll11l_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᇡ")][bstack1lll11l_opy_ (u"ࠢࡣࡵࡓࡥࡷࡧ࡭ࡴࠤᇢ")]
                    session_id = bstack1ll1ll11lll_opy_.get(bstack1lll11l_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡋࡧࠦᇣ"))
                    f.bstack1llll1ll11l_opy_(instance, bstack1lll1lll111_opy_.bstack1llll111l1l_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡦ࡬ࡷࡵࡧࡴࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࠧᇤ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll1l11_opy_(
        self,
        f: bstack1lll1lll111_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࠦᇥ"):
            return
        if not bstack1lll11l1lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡴࡴ࡮ࡦࡥࡷࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇦ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, connect, *args, **kwargs):
            response = self.bstack1llll1l11l1_opy_(f.platform_index, instance.ref(), json.dumps({bstack1lll11l_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᇧ"): True}).encode(bstack1lll11l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇨ")))
            if response is not None and response.capabilities:
                bstack1llll1lll11_opy_ = json.loads(response.capabilities.decode(bstack1lll11l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᇩ")))
                if not bstack1llll1lll11_opy_:
                    return
                bstack1ll1ll1l1ll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1lll11_opy_))
                if bstack1llll1lll11_opy_.get(bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᇪ")):
                    browser = bstack1ll1ll1lll1_opy_.connect_over_cdp(bstack1ll1ll1l1ll_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1ll1l1ll_opy_
                    return connect(bstack1ll1ll1lll1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1ll1llll_opy_(
        self,
        f: bstack1lll1lll111_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦᇫ"):
            return
        if not bstack1lll11l1lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡱࡩࡼࡥࡰࡢࡩࡨࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇬ"))
            return
        def wrapped(bstack1ll1llll111_opy_, bstack1ll1lll1111_opy_, *args, **kwargs):
            contexts = bstack1ll1llll111_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1lll11l_opy_ (u"ࠦࡦࡨ࡯ࡶࡶ࠽ࡦࡱࡧ࡮࡬ࠤᇭ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lll1111_opy_(bstack1ll1llll111_opy_)
        return wrapped
    def bstack1llll1l11l1_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥᇮ") + str(req) + bstack1lll11l_opy_ (u"ࠨࠢᇯ"))
        try:
            r = self.bstack1llll11l11l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥᇰ") + str(r.success) + bstack1lll11l_opy_ (u"ࠣࠤᇱ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᇲ") + str(e) + bstack1lll11l_opy_ (u"ࠥࠦᇳ"))
            traceback.print_exc()
            raise e
    def bstack1ll1ll1l111_opy_(
        self,
        f: bstack1lll1lll111_opy_,
        Connection: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠦࡤࡹࡥ࡯ࡦࡢࡱࡪࡹࡳࡢࡩࡨࡣࡹࡵ࡟ࡴࡧࡵࡺࡪࡸࠢᇴ"):
            return
        if not bstack1lll11l1lll_opy_():
            return
        def wrapped(Connection, bstack1ll1ll1l11l_opy_, *args, **kwargs):
            return bstack1ll1ll1l11l_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1lll111_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦᇵ"):
            return
        if not bstack1lll11l1lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡩ࡬ࡰࡵࡨࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇶ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped