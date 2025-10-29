# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import (
    bstack1ll1llllll1_opy_,
    bstack1llll1llll1_opy_,
    bstack1lllll1l1ll_opy_,
    bstack1llllll11ll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1l111l1_opy_(bstack1ll1llllll1_opy_):
    bstack1l1ll1ll11l_opy_ = bstack11l11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦዛ")
    bstack1lll1l1ll11_opy_ = bstack11l11ll_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧዜ")
    bstack1lll1llllll_opy_ = bstack11l11ll_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲࠢዝ")
    bstack1lll1llll11_opy_ = bstack11l11ll_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨዞ")
    bstack1l1lll111l1_opy_ = bstack11l11ll_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࠦዟ")
    bstack1l1lll11ll1_opy_ = bstack11l11ll_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࡦࡹࡹ࡯ࡥࠥዠ")
    NAME = bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢዡ")
    bstack1l1lll111ll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll111lll_opy_: Any
    bstack1l1ll1l1l1l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11l11ll_opy_ (u"ࠦࡱࡧࡵ࡯ࡥ࡫ࠦዢ"), bstack11l11ll_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࠨዣ"), bstack11l11ll_opy_ (u"ࠨ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠣዤ"), bstack11l11ll_opy_ (u"ࠢࡤ࡮ࡲࡷࡪࠨዥ"), bstack11l11ll_opy_ (u"ࠣࡦ࡬ࡷࡵࡧࡴࡤࡪࠥዦ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1ll1l11ll_opy_(methods)
    def bstack1l1ll1llll1_opy_(self, instance: bstack1llll1llll1_opy_, method_name: str, bstack1l1ll1l11l1_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1lll1111l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1ll1ll111_opy_, bstack1l1ll1l1ll1_opy_ = bstack1llll1ll1l1_opy_
        bstack1l1ll1l111l_opy_ = bstack1lll1l111l1_opy_.bstack1l1lll11111_opy_(bstack1llll1ll1l1_opy_)
        if bstack1l1ll1l111l_opy_ in bstack1lll1l111l1_opy_.bstack1l1lll111ll_opy_:
            bstack1l1ll1lllll_opy_ = None
            for callback in bstack1lll1l111l1_opy_.bstack1l1lll111ll_opy_[bstack1l1ll1l111l_opy_]:
                try:
                    bstack1l1ll1l1111_opy_ = callback(self, target, exec, bstack1llll1ll1l1_opy_, result, *args, **kwargs)
                    if bstack1l1ll1lllll_opy_ == None:
                        bstack1l1ll1lllll_opy_ = bstack1l1ll1l1111_opy_
                except Exception as e:
                    self.logger.error(bstack11l11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࠢዧ") + str(e) + bstack11l11ll_opy_ (u"ࠥࠦየ"))
                    traceback.print_exc()
            if bstack1l1ll1l1ll1_opy_ == bstack1llllll11ll_opy_.PRE and callable(bstack1l1ll1lllll_opy_):
                return bstack1l1ll1lllll_opy_
            elif bstack1l1ll1l1ll1_opy_ == bstack1llllll11ll_opy_.POST and bstack1l1ll1lllll_opy_:
                return bstack1l1ll1lllll_opy_
    def bstack1l1ll1lll11_opy_(
        self, method_name, previous_state: bstack1lllll1l1ll_opy_, *args, **kwargs
    ) -> bstack1lllll1l1ll_opy_:
        if method_name == bstack11l11ll_opy_ (u"ࠫࡱࡧࡵ࡯ࡥ࡫ࠫዩ") or method_name == bstack11l11ll_opy_ (u"ࠬࡩ࡯࡯ࡰࡨࡧࡹ࠭ዪ") or method_name == bstack11l11ll_opy_ (u"࠭࡮ࡦࡹࡢࡴࡦ࡭ࡥࠨያ"):
            return bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_
        if method_name == bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡴࡦࡺࡣࡩࠩዬ"):
            return bstack1lllll1l1ll_opy_.bstack1ll1ll1l111_opy_
        if method_name == bstack11l11ll_opy_ (u"ࠨࡥ࡯ࡳࡸ࡫ࠧይ"):
            return bstack1lllll1l1ll_opy_.QUIT
        return bstack1lllll1l1ll_opy_.NONE
    @staticmethod
    def bstack1l1lll11111_opy_(bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_]):
        return bstack11l11ll_opy_ (u"ࠤ࠽ࠦዮ").join((bstack1lllll1l1ll_opy_(bstack1llll1ll1l1_opy_[0]).name, bstack1llllll11ll_opy_(bstack1llll1ll1l1_opy_[1]).name))
    @staticmethod
    def bstack1llllll1l1l_opy_(bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_], callback: Callable):
        bstack1l1ll1l111l_opy_ = bstack1lll1l111l1_opy_.bstack1l1lll11111_opy_(bstack1llll1ll1l1_opy_)
        if not bstack1l1ll1l111l_opy_ in bstack1lll1l111l1_opy_.bstack1l1lll111ll_opy_:
            bstack1lll1l111l1_opy_.bstack1l1lll111ll_opy_[bstack1l1ll1l111l_opy_] = []
        bstack1lll1l111l1_opy_.bstack1l1lll111ll_opy_[bstack1l1ll1l111l_opy_].append(callback)
    @staticmethod
    def bstack1l1ll1ll1ll_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llll1lllll_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1llll1llll1_opy_, default_value=None):
        return bstack1ll1llllll1_opy_.get_state(instance, bstack1lll1l111l1_opy_.bstack1lll1llll11_opy_, default_value)
    @staticmethod
    def bstack1lll111111l_opy_(instance: bstack1llll1llll1_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1ll1l1l11_opy_(instance: bstack1llll1llll1_opy_, default_value=None):
        return bstack1ll1llllll1_opy_.get_state(instance, bstack1lll1l111l1_opy_.bstack1lll1llllll_opy_, default_value)
    @staticmethod
    def bstack1l1ll1l1lll_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll11lll_opy_(method_name: str, *args):
        if not bstack1lll1l111l1_opy_.bstack1l1ll1ll1ll_opy_(method_name):
            return False
        if not bstack1lll1l111l1_opy_.bstack1l1lll111l1_opy_ in bstack1lll1l111l1_opy_.bstack1lllll11l11_opy_(*args):
            return False
        bstack1l1lll11l1l_opy_ = bstack1lll1l111l1_opy_.bstack1l1ll1lll1l_opy_(*args)
        return bstack1l1lll11l1l_opy_ and bstack11l11ll_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዯ") in bstack1l1lll11l1l_opy_ and bstack11l11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧደ") in bstack1l1lll11l1l_opy_[bstack11l11ll_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧዱ")]
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(method_name: str, *args):
        if not bstack1lll1l111l1_opy_.bstack1l1ll1ll1ll_opy_(method_name):
            return False
        if not bstack1lll1l111l1_opy_.bstack1l1lll111l1_opy_ in bstack1lll1l111l1_opy_.bstack1lllll11l11_opy_(*args):
            return False
        bstack1l1lll11l1l_opy_ = bstack1lll1l111l1_opy_.bstack1l1ll1lll1l_opy_(*args)
        return (
            bstack1l1lll11l1l_opy_
            and bstack11l11ll_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨዲ") in bstack1l1lll11l1l_opy_
            and bstack11l11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡨࡸࡩࡱࡶࠥዳ") in bstack1l1lll11l1l_opy_[bstack11l11ll_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣዴ")]
        )
    @staticmethod
    def bstack1lllll11l11_opy_(*args):
        return str(bstack1lll1l111l1_opy_.bstack1l1ll1l1lll_opy_(*args)).lower()