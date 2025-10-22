# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lll1111l1l_opy_,
    bstack1lllll111l1_opy_,
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1l1l1ll_opy_(bstack1lll1111l1l_opy_):
    bstack1l1lll1l111_opy_ = bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥዌ")
    bstack1lll1llll1l_opy_ = bstack1lllll1l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦው")
    bstack1lll1lllll1_opy_ = bstack1lllll1l_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࠨዎ")
    bstack1llll111l11_opy_ = bstack1lllll1l_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧዏ")
    bstack1l1ll1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥዐ")
    bstack1l1ll1l1lll_opy_ = bstack1lllll1l_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤዑ")
    NAME = bstack1lllll1l_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨዒ")
    bstack1l1ll1ll111_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1ll11l_opy_: Any
    bstack1l1lll1l1l1_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1lllll1l_opy_ (u"ࠥࡰࡦࡻ࡮ࡤࡪࠥዓ"), bstack1lllll1l_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࠧዔ"), bstack1lllll1l_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢዕ"), bstack1lllll1l_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧዖ"), bstack1lllll1l_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤ዗")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1lll11lll_opy_(methods)
    def bstack1l1ll1l1l1l_opy_(self, instance: bstack1lllll111l1_opy_, method_name: str, bstack1l1ll1ll1ll_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1ll1lll11_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll111l1_opy_, bstack1l1lll11111_opy_ = bstack1llll1l1lll_opy_
        bstack1l1lll1l1ll_opy_ = bstack1lll1l1l1ll_opy_.bstack1l1lll11ll1_opy_(bstack1llll1l1lll_opy_)
        if bstack1l1lll1l1ll_opy_ in bstack1lll1l1l1ll_opy_.bstack1l1ll1ll111_opy_:
            bstack1l1ll1ll11l_opy_ = None
            for callback in bstack1lll1l1l1ll_opy_.bstack1l1ll1ll111_opy_[bstack1l1lll1l1ll_opy_]:
                try:
                    bstack1l1lll11l1l_opy_ = callback(self, target, exec, bstack1llll1l1lll_opy_, result, *args, **kwargs)
                    if bstack1l1ll1ll11l_opy_ == None:
                        bstack1l1ll1ll11l_opy_ = bstack1l1lll11l1l_opy_
                except Exception as e:
                    self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨዘ") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥዙ"))
                    traceback.print_exc()
            if bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.PRE and callable(bstack1l1ll1ll11l_opy_):
                return bstack1l1ll1ll11l_opy_
            elif bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.POST and bstack1l1ll1ll11l_opy_:
                return bstack1l1ll1ll11l_opy_
    def bstack1l1lll1l11l_opy_(
        self, method_name, previous_state: bstack1lllllll1l1_opy_, *args, **kwargs
    ) -> bstack1lllllll1l1_opy_:
        if method_name == bstack1lllll1l_opy_ (u"ࠪࡰࡦࡻ࡮ࡤࡪࠪዚ") or method_name == bstack1lllll1l_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࠬዛ") or method_name == bstack1lllll1l_opy_ (u"ࠬࡴࡥࡸࡡࡳࡥ࡬࡫ࠧዜ"):
            return bstack1lllllll1l1_opy_.bstack1lllll11111_opy_
        if method_name == bstack1lllll1l_opy_ (u"࠭ࡤࡪࡵࡳࡥࡹࡩࡨࠨዝ"):
            return bstack1lllllll1l1_opy_.bstack1ll1lll11l1_opy_
        if method_name == bstack1lllll1l_opy_ (u"ࠧࡤ࡮ࡲࡷࡪ࠭ዞ"):
            return bstack1lllllll1l1_opy_.QUIT
        return bstack1lllllll1l1_opy_.NONE
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_]):
        return bstack1lllll1l_opy_ (u"ࠣ࠼ࠥዟ").join((bstack1lllllll1l1_opy_(bstack1llll1l1lll_opy_[0]).name, bstack1llllll1l11_opy_(bstack1llll1l1lll_opy_[1]).name))
    @staticmethod
    def bstack1llll1l1l11_opy_(bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_], callback: Callable):
        bstack1l1lll1l1ll_opy_ = bstack1lll1l1l1ll_opy_.bstack1l1lll11ll1_opy_(bstack1llll1l1lll_opy_)
        if not bstack1l1lll1l1ll_opy_ in bstack1lll1l1l1ll_opy_.bstack1l1ll1ll111_opy_:
            bstack1lll1l1l1ll_opy_.bstack1l1ll1ll111_opy_[bstack1l1lll1l1ll_opy_] = []
        bstack1lll1l1l1ll_opy_.bstack1l1ll1ll111_opy_[bstack1l1lll1l1ll_opy_].append(callback)
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llll1l1ll1_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1ll1lllll_opy_(instance: bstack1lllll111l1_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1lll1l1l1ll_opy_.bstack1llll111l11_opy_, default_value)
    @staticmethod
    def bstack1lll1111lll_opy_(instance: bstack1lllll111l1_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1ll1llll1_opy_(instance: bstack1lllll111l1_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1lll1l1l1ll_opy_.bstack1lll1lllll1_opy_, default_value)
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1lll1l_opy_(method_name: str, *args):
        if not bstack1lll1l1l1ll_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1lll1l1l1ll_opy_.bstack1l1ll1l1l11_opy_ in bstack1lll1l1l1ll_opy_.bstack1llllllll11_opy_(*args):
            return False
        bstack1l1ll1l1ll1_opy_ = bstack1lll1l1l1ll_opy_.bstack1l1lll1111l_opy_(*args)
        return bstack1l1ll1l1ll1_opy_ and bstack1lllll1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤዠ") in bstack1l1ll1l1ll1_opy_ and bstack1lllll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦዡ") in bstack1l1ll1l1ll1_opy_[bstack1lllll1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦዢ")]
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1lll1l1l1ll_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1lll1l1l1ll_opy_.bstack1l1ll1l1l11_opy_ in bstack1lll1l1l1ll_opy_.bstack1llllllll11_opy_(*args):
            return False
        bstack1l1ll1l1ll1_opy_ = bstack1lll1l1l1ll_opy_.bstack1l1lll1111l_opy_(*args)
        return (
            bstack1l1ll1l1ll1_opy_
            and bstack1lllll1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧዣ") in bstack1l1ll1l1ll1_opy_
            and bstack1lllll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤዤ") in bstack1l1ll1l1ll1_opy_[bstack1lllll1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዥ")]
        )
    @staticmethod
    def bstack1llllllll11_opy_(*args):
        return str(bstack1lll1l1l1ll_opy_.bstack1l1ll1ll1l1_opy_(*args)).lower()