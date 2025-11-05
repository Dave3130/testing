# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1lll1111l11_opy_,
    bstack1llll111l1l_opy_,
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll11l1l11_opy_(bstack1lll1111l11_opy_):
    bstack1l1ll1lllll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤዠ")
    bstack1lll11l1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥዡ")
    bstack1lll11lll1l_opy_ = bstack11ll1ll_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࠧዢ")
    bstack1lll11ll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦዣ")
    bstack1l1ll1l11ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࠤዤ")
    bstack1l1ll1ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࡤࡷࡾࡴࡣࠣዥ")
    NAME = bstack11ll1ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧዦ")
    bstack1l1ll1l1111_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1ll1ll_opy_: Any
    bstack1l1ll1lll11_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11ll1ll_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤዧ"), bstack11ll1ll_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࠦየ"), bstack11ll1ll_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨዩ"), bstack11ll1ll_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦዪ"), bstack11ll1ll_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣያ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1lll1111l_opy_(methods)
    def bstack1l1ll1ll1l1_opy_(self, instance: bstack1llll111l1l_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1lll111l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1ll1l11l1_opy_, bstack1l1ll1l1l1l_opy_ = bstack1lllllllll1_opy_
        bstack1l1ll1llll1_opy_ = bstack1lll11l1l11_opy_.bstack1l1ll1l111l_opy_(bstack1lllllllll1_opy_)
        if bstack1l1ll1llll1_opy_ in bstack1lll11l1l11_opy_.bstack1l1ll1l1111_opy_:
            bstack1l1ll1ll111_opy_ = None
            for callback in bstack1lll11l1l11_opy_.bstack1l1ll1l1111_opy_[bstack1l1ll1llll1_opy_]:
                try:
                    bstack1l1ll1ll11l_opy_ = callback(self, target, exec, bstack1lllllllll1_opy_, result, *args, **kwargs)
                    if bstack1l1ll1ll111_opy_ == None:
                        bstack1l1ll1ll111_opy_ = bstack1l1ll1ll11l_opy_
                except Exception as e:
                    self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࠧዬ") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤይ"))
                    traceback.print_exc()
            if bstack1l1ll1l1l1l_opy_ == bstack1llll11llll_opy_.PRE and callable(bstack1l1ll1ll111_opy_):
                return bstack1l1ll1ll111_opy_
            elif bstack1l1ll1l1l1l_opy_ == bstack1llll11llll_opy_.POST and bstack1l1ll1ll111_opy_:
                return bstack1l1ll1ll111_opy_
    def bstack1l1ll1l1l11_opy_(
        self, method_name, previous_state: bstack1llll1l1ll1_opy_, *args, **kwargs
    ) -> bstack1llll1l1ll1_opy_:
        if method_name == bstack11ll1ll_opy_ (u"ࠩ࡯ࡥࡺࡴࡣࡩࠩዮ") or method_name == bstack11ll1ll_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࠫዯ") or method_name == bstack11ll1ll_opy_ (u"ࠫࡳ࡫ࡷࡠࡲࡤ࡫ࡪ࠭ደ"):
            return bstack1llll1l1ll1_opy_.bstack1llllllll1l_opy_
        if method_name == bstack11ll1ll_opy_ (u"ࠬࡪࡩࡴࡲࡤࡸࡨ࡮ࠧዱ"):
            return bstack1llll1l1ll1_opy_.bstack1ll1ll11lll_opy_
        if method_name == bstack11ll1ll_opy_ (u"࠭ࡣ࡭ࡱࡶࡩࠬዲ"):
            return bstack1llll1l1ll1_opy_.QUIT
        return bstack1llll1l1ll1_opy_.NONE
    @staticmethod
    def bstack1l1ll1l111l_opy_(bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_]):
        return bstack11ll1ll_opy_ (u"ࠢ࠻ࠤዳ").join((bstack1llll1l1ll1_opy_(bstack1lllllllll1_opy_[0]).name, bstack1llll11llll_opy_(bstack1lllllllll1_opy_[1]).name))
    @staticmethod
    def bstack1lllll1l11l_opy_(bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_], callback: Callable):
        bstack1l1ll1llll1_opy_ = bstack1lll11l1l11_opy_.bstack1l1ll1l111l_opy_(bstack1lllllllll1_opy_)
        if not bstack1l1ll1llll1_opy_ in bstack1lll11l1l11_opy_.bstack1l1ll1l1111_opy_:
            bstack1lll11l1l11_opy_.bstack1l1ll1l1111_opy_[bstack1l1ll1llll1_opy_] = []
        bstack1lll11l1l11_opy_.bstack1l1ll1l1111_opy_[bstack1l1ll1llll1_opy_].append(callback)
    @staticmethod
    def bstack1l1lll11ll1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llll1l1111_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1ll11llll_opy_(instance: bstack1llll111l1l_opy_, default_value=None):
        return bstack1lll1111l11_opy_.get_state(instance, bstack1lll11l1l11_opy_.bstack1lll11ll1l1_opy_, default_value)
    @staticmethod
    def bstack1lll1111l1l_opy_(instance: bstack1llll111l1l_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll111ll_opy_(instance: bstack1llll111l1l_opy_, default_value=None):
        return bstack1lll1111l11_opy_.get_state(instance, bstack1lll11l1l11_opy_.bstack1lll11lll1l_opy_, default_value)
    @staticmethod
    def bstack1l1ll1lll1l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1l1lll_opy_(method_name: str, *args):
        if not bstack1lll11l1l11_opy_.bstack1l1lll11ll1_opy_(method_name):
            return False
        if not bstack1lll11l1l11_opy_.bstack1l1ll1l11ll_opy_ in bstack1lll11l1l11_opy_.bstack1llll1ll1l1_opy_(*args):
            return False
        bstack1l1lll11l1l_opy_ = bstack1lll11l1l11_opy_.bstack1l1ll1l1ll1_opy_(*args)
        return bstack1l1lll11l1l_opy_ and bstack11ll1ll_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣዴ") in bstack1l1lll11l1l_opy_ and bstack11ll1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥድ") in bstack1l1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዶ")]
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str, *args):
        if not bstack1lll11l1l11_opy_.bstack1l1lll11ll1_opy_(method_name):
            return False
        if not bstack1lll11l1l11_opy_.bstack1l1ll1l11ll_opy_ in bstack1lll11l1l11_opy_.bstack1llll1ll1l1_opy_(*args):
            return False
        bstack1l1lll11l1l_opy_ = bstack1lll11l1l11_opy_.bstack1l1ll1l1ll1_opy_(*args)
        return (
            bstack1l1lll11l1l_opy_
            and bstack11ll1ll_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦዷ") in bstack1l1lll11l1l_opy_
            and bstack11ll1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡦࡶ࡮ࡶࡴࠣዸ") in bstack1l1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨዹ")]
        )
    @staticmethod
    def bstack1llll1ll1l1_opy_(*args):
        return str(bstack1lll11l1l11_opy_.bstack1l1ll1lll1l_opy_(*args)).lower()