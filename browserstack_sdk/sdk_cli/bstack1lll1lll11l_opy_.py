# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import (
    bstack1lll1111l1l_opy_,
    bstack1llll111l1l_opy_,
    bstack1lllllll1l1_opy_,
    bstack1llllll1111_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1llll11111l_opy_(bstack1lll1111l1l_opy_):
    bstack1l1ll1ll11l_opy_ = bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣዟ")
    bstack1lll11l1l1l_opy_ = bstack11111_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤዠ")
    bstack1lll1l11ll1_opy_ = bstack11111_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦዡ")
    bstack1lll11lll11_opy_ = bstack11111_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥዢ")
    bstack1l1ll1llll1_opy_ = bstack11111_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࠣዣ")
    bstack1l1ll1ll1ll_opy_ = bstack11111_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࡣࡶࡽࡳࡩࠢዤ")
    NAME = bstack11111_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦዥ")
    bstack1l1lll11l1l_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1lllll_opy_: Any
    bstack1l1ll1l1l11_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11111_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣዦ"), bstack11111_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥዧ"), bstack11111_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧየ"), bstack11111_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥዩ"), bstack11111_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢዪ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1ll1lll11_opy_(methods)
    def bstack1l1ll1ll111_opy_(self, instance: bstack1llll111l1l_opy_, method_name: str, bstack1l1ll11llll_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1ll1l111l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll11ll1_opy_, bstack1l1lll1111l_opy_ = bstack1llll11ll1l_opy_
        bstack1l1ll1lllll_opy_ = bstack1llll11111l_opy_.bstack1l1ll1l1ll1_opy_(bstack1llll11ll1l_opy_)
        if bstack1l1ll1lllll_opy_ in bstack1llll11111l_opy_.bstack1l1lll11l1l_opy_:
            bstack1l1ll1l1111_opy_ = None
            for callback in bstack1llll11111l_opy_.bstack1l1lll11l1l_opy_[bstack1l1ll1lllll_opy_]:
                try:
                    bstack1l1lll111ll_opy_ = callback(self, target, exec, bstack1llll11ll1l_opy_, result, *args, **kwargs)
                    if bstack1l1ll1l1111_opy_ == None:
                        bstack1l1ll1l1111_opy_ = bstack1l1lll111ll_opy_
                except Exception as e:
                    self.logger.error(bstack11111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࠦያ") + str(e) + bstack11111_opy_ (u"ࠢࠣዬ"))
                    traceback.print_exc()
            if bstack1l1lll1111l_opy_ == bstack1llllll1111_opy_.PRE and callable(bstack1l1ll1l1111_opy_):
                return bstack1l1ll1l1111_opy_
            elif bstack1l1lll1111l_opy_ == bstack1llllll1111_opy_.POST and bstack1l1ll1l1111_opy_:
                return bstack1l1ll1l1111_opy_
    def bstack1l1ll1l11ll_opy_(
        self, method_name, previous_state: bstack1lllllll1l1_opy_, *args, **kwargs
    ) -> bstack1lllllll1l1_opy_:
        if method_name == bstack11111_opy_ (u"ࠨ࡮ࡤࡹࡳࡩࡨࠨይ") or method_name == bstack11111_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࠪዮ") or method_name == bstack11111_opy_ (u"ࠪࡲࡪࡽ࡟ࡱࡣࡪࡩࠬዯ"):
            return bstack1lllllll1l1_opy_.bstack1llll11llll_opy_
        if method_name == bstack11111_opy_ (u"ࠫࡩ࡯ࡳࡱࡣࡷࡧ࡭࠭ደ"):
            return bstack1lllllll1l1_opy_.bstack1ll1ll11lll_opy_
        if method_name == bstack11111_opy_ (u"ࠬࡩ࡬ࡰࡵࡨࠫዱ"):
            return bstack1lllllll1l1_opy_.QUIT
        return bstack1lllllll1l1_opy_.NONE
    @staticmethod
    def bstack1l1ll1l1ll1_opy_(bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_]):
        return bstack11111_opy_ (u"ࠨ࠺ࠣዲ").join((bstack1lllllll1l1_opy_(bstack1llll11ll1l_opy_[0]).name, bstack1llllll1111_opy_(bstack1llll11ll1l_opy_[1]).name))
    @staticmethod
    def bstack1llll11ll11_opy_(bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_], callback: Callable):
        bstack1l1ll1lllll_opy_ = bstack1llll11111l_opy_.bstack1l1ll1l1ll1_opy_(bstack1llll11ll1l_opy_)
        if not bstack1l1ll1lllll_opy_ in bstack1llll11111l_opy_.bstack1l1lll11l1l_opy_:
            bstack1llll11111l_opy_.bstack1l1lll11l1l_opy_[bstack1l1ll1lllll_opy_] = []
        bstack1llll11111l_opy_.bstack1l1lll11l1l_opy_[bstack1l1ll1lllll_opy_].append(callback)
    @staticmethod
    def bstack1l1ll1l1lll_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llllll11ll_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1llll111l1l_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll11111l_opy_.bstack1lll11lll11_opy_, default_value)
    @staticmethod
    def bstack1lll11111ll_opy_(instance: bstack1llll111l1l_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(instance: bstack1llll111l1l_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll11111l_opy_.bstack1lll1l11ll1_opy_, default_value)
    @staticmethod
    def bstack1l1ll1lll1l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll111l1_opy_(method_name: str, *args):
        if not bstack1llll11111l_opy_.bstack1l1ll1l1lll_opy_(method_name):
            return False
        if not bstack1llll11111l_opy_.bstack1l1ll1llll1_opy_ in bstack1llll11111l_opy_.bstack1llll1ll111_opy_(*args):
            return False
        bstack1l1ll1l11l1_opy_ = bstack1llll11111l_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return bstack1l1ll1l11l1_opy_ and bstack11111_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዳ") in bstack1l1ll1l11l1_opy_ and bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤዴ") in bstack1l1ll1l11l1_opy_[bstack11111_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤድ")]
    @staticmethod
    def bstack1l1lll11111_opy_(method_name: str, *args):
        if not bstack1llll11111l_opy_.bstack1l1ll1l1lll_opy_(method_name):
            return False
        if not bstack1llll11111l_opy_.bstack1l1ll1llll1_opy_ in bstack1llll11111l_opy_.bstack1llll1ll111_opy_(*args):
            return False
        bstack1l1ll1l11l1_opy_ = bstack1llll11111l_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return (
            bstack1l1ll1l11l1_opy_
            and bstack11111_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዶ") in bstack1l1ll1l11l1_opy_
            and bstack11111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡥࡵ࡭ࡵࡺࠢዷ") in bstack1l1ll1l11l1_opy_[bstack11111_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧዸ")]
        )
    @staticmethod
    def bstack1llll1ll111_opy_(*args):
        return str(bstack1llll11111l_opy_.bstack1l1ll1lll1l_opy_(*args)).lower()