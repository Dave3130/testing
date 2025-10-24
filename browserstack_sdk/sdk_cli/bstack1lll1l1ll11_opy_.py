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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import (
    bstack1lll11111ll_opy_,
    bstack1llllll1l1l_opy_,
    bstack1llllll111l_opy_,
    bstack1llll1l111l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1llll111l11_opy_(bstack1lll11111ll_opy_):
    bstack1l1lll11111_opy_ = bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨ዁")
    bstack1lll11ll11l_opy_ = bstack1l1_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢዂ")
    bstack1lll1l1l11l_opy_ = bstack1l1_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭ࠤዃ")
    bstack1lll11lll11_opy_ = bstack1l1_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣዄ")
    bstack1l1lll1l1l1_opy_ = bstack1l1_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࠨዅ")
    bstack1l1ll1lll11_opy_ = bstack1l1_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࡡࡴࡻࡱࡧࠧ዆")
    NAME = bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ዇")
    bstack1l1lll11l11_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll11l1l_opy_: Any
    bstack1l1lll1l11l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1l1_opy_ (u"ࠨ࡬ࡢࡷࡱࡧ࡭ࠨወ"), bstack1l1_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣዉ"), bstack1l1_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥዊ"), bstack1l1_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣዋ"), bstack1l1_opy_ (u"ࠥࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠧዌ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1lll1l111_opy_(methods)
    def bstack1l1lll1ll1l_opy_(self, instance: bstack1llllll1l1l_opy_, method_name: str, bstack1l1ll1ll111_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1ll1lllll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1ll1ll1ll_opy_, bstack1l1lll1ll11_opy_ = bstack1lllll1l1l1_opy_
        bstack1l1lll1l1ll_opy_ = bstack1llll111l11_opy_.bstack1l1lll111ll_opy_(bstack1lllll1l1l1_opy_)
        if bstack1l1lll1l1ll_opy_ in bstack1llll111l11_opy_.bstack1l1lll11l11_opy_:
            bstack1l1lll1111l_opy_ = None
            for callback in bstack1llll111l11_opy_.bstack1l1lll11l11_opy_[bstack1l1lll1l1ll_opy_]:
                try:
                    bstack1l1ll1l1ll1_opy_ = callback(self, target, exec, bstack1lllll1l1l1_opy_, result, *args, **kwargs)
                    if bstack1l1lll1111l_opy_ == None:
                        bstack1l1lll1111l_opy_ = bstack1l1ll1l1ll1_opy_
                except Exception as e:
                    self.logger.error(bstack1l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࠤው") + str(e) + bstack1l1_opy_ (u"ࠧࠨዎ"))
                    traceback.print_exc()
            if bstack1l1lll1ll11_opy_ == bstack1llll1l111l_opy_.PRE and callable(bstack1l1lll1111l_opy_):
                return bstack1l1lll1111l_opy_
            elif bstack1l1lll1ll11_opy_ == bstack1llll1l111l_opy_.POST and bstack1l1lll1111l_opy_:
                return bstack1l1lll1111l_opy_
    def bstack1l1lll11l1l_opy_(
        self, method_name, previous_state: bstack1llllll111l_opy_, *args, **kwargs
    ) -> bstack1llllll111l_opy_:
        if method_name == bstack1l1_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࠭ዏ") or method_name == bstack1l1_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨዐ") or method_name == bstack1l1_opy_ (u"ࠨࡰࡨࡻࡤࡶࡡࡨࡧࠪዑ"):
            return bstack1llllll111l_opy_.bstack1lllll1ll11_opy_
        if method_name == bstack1l1_opy_ (u"ࠩࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠫዒ"):
            return bstack1llllll111l_opy_.bstack1ll1lll1l11_opy_
        if method_name == bstack1l1_opy_ (u"ࠪࡧࡱࡵࡳࡦࠩዓ"):
            return bstack1llllll111l_opy_.QUIT
        return bstack1llllll111l_opy_.NONE
    @staticmethod
    def bstack1l1lll111ll_opy_(bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_]):
        return bstack1l1_opy_ (u"ࠦ࠿ࠨዔ").join((bstack1llllll111l_opy_(bstack1lllll1l1l1_opy_[0]).name, bstack1llll1l111l_opy_(bstack1lllll1l1l1_opy_[1]).name))
    @staticmethod
    def bstack1llll1ll1l1_opy_(bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_], callback: Callable):
        bstack1l1lll1l1ll_opy_ = bstack1llll111l11_opy_.bstack1l1lll111ll_opy_(bstack1lllll1l1l1_opy_)
        if not bstack1l1lll1l1ll_opy_ in bstack1llll111l11_opy_.bstack1l1lll11l11_opy_:
            bstack1llll111l11_opy_.bstack1l1lll11l11_opy_[bstack1l1lll1l1ll_opy_] = []
        bstack1llll111l11_opy_.bstack1l1lll11l11_opy_[bstack1l1lll1l1ll_opy_].append(callback)
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llll1ll11l_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1ll1l1lll_opy_(instance: bstack1llllll1l1l_opy_, default_value=None):
        return bstack1lll11111ll_opy_.get_state(instance, bstack1llll111l11_opy_.bstack1lll11lll11_opy_, default_value)
    @staticmethod
    def bstack1lll111l11l_opy_(instance: bstack1llllll1l1l_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll111l1_opy_(instance: bstack1llllll1l1l_opy_, default_value=None):
        return bstack1lll11111ll_opy_.get_state(instance, bstack1llll111l11_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1l1lll11ll1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1ll11l_opy_(method_name: str, *args):
        if not bstack1llll111l11_opy_.bstack1l1ll1ll1l1_opy_(method_name):
            return False
        if not bstack1llll111l11_opy_.bstack1l1lll1l1l1_opy_ in bstack1llll111l11_opy_.bstack1llll1l1ll1_opy_(*args):
            return False
        bstack1l1ll1lll1l_opy_ = bstack1llll111l11_opy_.bstack1l1ll1llll1_opy_(*args)
        return bstack1l1ll1lll1l_opy_ and bstack1l1_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧዕ") in bstack1l1ll1lll1l_opy_ and bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢዖ") in bstack1l1ll1lll1l_opy_[bstack1l1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢ዗")]
    @staticmethod
    def bstack1l1lll11lll_opy_(method_name: str, *args):
        if not bstack1llll111l11_opy_.bstack1l1ll1ll1l1_opy_(method_name):
            return False
        if not bstack1llll111l11_opy_.bstack1l1lll1l1l1_opy_ in bstack1llll111l11_opy_.bstack1llll1l1ll1_opy_(*args):
            return False
        bstack1l1ll1lll1l_opy_ = bstack1llll111l11_opy_.bstack1l1ll1llll1_opy_(*args)
        return (
            bstack1l1ll1lll1l_opy_
            and bstack1l1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣዘ") in bstack1l1ll1lll1l_opy_
            and bstack1l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡣࡳ࡫ࡳࡸࠧዙ") in bstack1l1ll1lll1l_opy_[bstack1l1_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዚ")]
        )
    @staticmethod
    def bstack1llll1l1ll1_opy_(*args):
        return str(bstack1llll111l11_opy_.bstack1l1lll11ll1_opy_(*args)).lower()