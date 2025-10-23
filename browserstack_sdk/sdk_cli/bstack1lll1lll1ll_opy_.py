# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lll1111lll_opy_,
    bstack1llll11l11l_opy_,
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1l1l1l1_opy_(bstack1lll1111lll_opy_):
    bstack1l1ll1ll1ll_opy_ = bstack11lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨወ")
    bstack1lll1l1l1ll_opy_ = bstack11lll1_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢዉ")
    bstack1lll1l1l11l_opy_ = bstack11lll1_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭ࠤዊ")
    bstack1lll11ll1ll_opy_ = bstack11lll1_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣዋ")
    bstack1l1ll1l1l11_opy_ = bstack11lll1_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࠨዌ")
    bstack1l1lll11l11_opy_ = bstack11lll1_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࡡࡴࡻࡱࡧࠧው")
    NAME = bstack11lll1_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤዎ")
    bstack1l1ll1lllll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1l111l_opy_: Any
    bstack1l1ll1ll11l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11lll1_opy_ (u"ࠨ࡬ࡢࡷࡱࡧ࡭ࠨዏ"), bstack11lll1_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣዐ"), bstack11lll1_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥዑ"), bstack11lll1_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣዒ"), bstack11lll1_opy_ (u"ࠥࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠧዓ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1ll1llll1_opy_(methods)
    def bstack1l1lll11111_opy_(self, instance: bstack1llll11l11l_opy_, method_name: str, bstack1l1lll1111l_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1lll1l1l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll111ll_opy_, bstack1l1lll11ll1_opy_ = bstack1llll1lll1l_opy_
        bstack1l1ll1ll111_opy_ = bstack1lll1l1l1l1_opy_.bstack1l1ll1l11ll_opy_(bstack1llll1lll1l_opy_)
        if bstack1l1ll1ll111_opy_ in bstack1lll1l1l1l1_opy_.bstack1l1ll1lllll_opy_:
            bstack1l1ll1lll1l_opy_ = None
            for callback in bstack1lll1l1l1l1_opy_.bstack1l1ll1lllll_opy_[bstack1l1ll1ll111_opy_]:
                try:
                    bstack1l1ll1l1ll1_opy_ = callback(self, target, exec, bstack1llll1lll1l_opy_, result, *args, **kwargs)
                    if bstack1l1ll1lll1l_opy_ == None:
                        bstack1l1ll1lll1l_opy_ = bstack1l1ll1l1ll1_opy_
                except Exception as e:
                    self.logger.error(bstack11lll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࠤዔ") + str(e) + bstack11lll1_opy_ (u"ࠧࠨዕ"))
                    traceback.print_exc()
            if bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.PRE and callable(bstack1l1ll1lll1l_opy_):
                return bstack1l1ll1lll1l_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.POST and bstack1l1ll1lll1l_opy_:
                return bstack1l1ll1lll1l_opy_
    def bstack1l1lll11l1l_opy_(
        self, method_name, previous_state: bstack1lllll111ll_opy_, *args, **kwargs
    ) -> bstack1lllll111ll_opy_:
        if method_name == bstack11lll1_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࠭ዖ") or method_name == bstack11lll1_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨ዗") or method_name == bstack11lll1_opy_ (u"ࠨࡰࡨࡻࡤࡶࡡࡨࡧࠪዘ"):
            return bstack1lllll111ll_opy_.bstack1llllll1lll_opy_
        if method_name == bstack11lll1_opy_ (u"ࠩࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠫዙ"):
            return bstack1lllll111ll_opy_.bstack1ll1lll111l_opy_
        if method_name == bstack11lll1_opy_ (u"ࠪࡧࡱࡵࡳࡦࠩዚ"):
            return bstack1lllll111ll_opy_.QUIT
        return bstack1lllll111ll_opy_.NONE
    @staticmethod
    def bstack1l1ll1l11ll_opy_(bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_]):
        return bstack11lll1_opy_ (u"ࠦ࠿ࠨዛ").join((bstack1lllll111ll_opy_(bstack1llll1lll1l_opy_[0]).name, bstack1llllll1l11_opy_(bstack1llll1lll1l_opy_[1]).name))
    @staticmethod
    def bstack1lllll1llll_opy_(bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_], callback: Callable):
        bstack1l1ll1ll111_opy_ = bstack1lll1l1l1l1_opy_.bstack1l1ll1l11ll_opy_(bstack1llll1lll1l_opy_)
        if not bstack1l1ll1ll111_opy_ in bstack1lll1l1l1l1_opy_.bstack1l1ll1lllll_opy_:
            bstack1lll1l1l1l1_opy_.bstack1l1ll1lllll_opy_[bstack1l1ll1ll111_opy_] = []
        bstack1lll1l1l1l1_opy_.bstack1l1ll1lllll_opy_[bstack1l1ll1ll111_opy_].append(callback)
    @staticmethod
    def bstack1l1lll111l1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llll11l1ll_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1ll1l1lll_opy_(instance: bstack1llll11l11l_opy_, default_value=None):
        return bstack1lll1111lll_opy_.get_state(instance, bstack1lll1l1l1l1_opy_.bstack1lll11ll1ll_opy_, default_value)
    @staticmethod
    def bstack1lll111l1ll_opy_(instance: bstack1llll11l11l_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1l111_opy_(instance: bstack1llll11l11l_opy_, default_value=None):
        return bstack1lll1111lll_opy_.get_state(instance, bstack1lll1l1l1l1_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1l1lll1l11l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(method_name: str, *args):
        if not bstack1lll1l1l1l1_opy_.bstack1l1lll111l1_opy_(method_name):
            return False
        if not bstack1lll1l1l1l1_opy_.bstack1l1ll1l1l11_opy_ in bstack1lll1l1l1l1_opy_.bstack1llll11ll11_opy_(*args):
            return False
        bstack1l1ll1lll11_opy_ = bstack1lll1l1l1l1_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return bstack1l1ll1lll11_opy_ and bstack11lll1_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧዜ") in bstack1l1ll1lll11_opy_ and bstack11lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢዝ") in bstack1l1ll1lll11_opy_[bstack11lll1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዞ")]
    @staticmethod
    def bstack1l1lll11lll_opy_(method_name: str, *args):
        if not bstack1lll1l1l1l1_opy_.bstack1l1lll111l1_opy_(method_name):
            return False
        if not bstack1lll1l1l1l1_opy_.bstack1l1ll1l1l11_opy_ in bstack1lll1l1l1l1_opy_.bstack1llll11ll11_opy_(*args):
            return False
        bstack1l1ll1lll11_opy_ = bstack1lll1l1l1l1_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return (
            bstack1l1ll1lll11_opy_
            and bstack11lll1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣዟ") in bstack1l1ll1lll11_opy_
            and bstack11lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡣࡳ࡫ࡳࡸࠧዠ") in bstack1l1ll1lll11_opy_[bstack11lll1_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዡ")]
        )
    @staticmethod
    def bstack1llll11ll11_opy_(*args):
        return str(bstack1lll1l1l1l1_opy_.bstack1l1lll1l11l_opy_(*args)).lower()