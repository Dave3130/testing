# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lll11ll1l1_opy_,
    bstack111111lll1_opy_,
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1llll1l11ll_opy_(bstack1lll11ll1l1_opy_):
    bstack1l1llll11ll_opy_ = bstack1ll11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧካ")
    bstack1lll1ll1l11_opy_ = bstack1ll11_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨኬ")
    bstack1lll1l1l1ll_opy_ = bstack1ll11_opy_ (u"ࠢࡩࡷࡥࡣࡺࡸ࡬ࠣክ")
    bstack1lll1l1lll1_opy_ = bstack1ll11_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢኮ")
    bstack1l1lll11lll_opy_ = bstack1ll11_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࠧኯ")
    bstack1l1ll1lllll_opy_ = bstack1ll11_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࡧࡳࡺࡰࡦࠦኰ")
    NAME = bstack1ll11_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ኱")
    bstack1l1lll11l1l_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1111111l11_opy_: Any
    bstack1l1lll1ll1l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1ll11_opy_ (u"ࠧࡲࡡࡶࡰࡦ࡬ࠧኲ"), bstack1ll11_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢኳ"), bstack1ll11_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤኴ"), bstack1ll11_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢኵ"), bstack1ll11_opy_ (u"ࠤࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠦ኶")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1lll1l1l1_opy_(methods)
    def bstack1l1lll1l11l_opy_(self, instance: bstack111111lll1_opy_, method_name: str, bstack1l1llll1ll1_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1llll11l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll111l_opy_, bstack1l1llll1l1l_opy_ = bstack1llll1l1ll1_opy_
        bstack1l1lll1l111_opy_ = bstack1llll1l11ll_opy_.bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_)
        if bstack1l1lll1l111_opy_ in bstack1llll1l11ll_opy_.bstack1l1lll11l1l_opy_:
            bstack1l1llll1l11_opy_ = None
            for callback in bstack1llll1l11ll_opy_.bstack1l1lll11l1l_opy_[bstack1l1lll1l111_opy_]:
                try:
                    bstack1l1lll1l1ll_opy_ = callback(self, target, exec, bstack1llll1l1ll1_opy_, result, *args, **kwargs)
                    if bstack1l1llll1l11_opy_ == None:
                        bstack1l1llll1l11_opy_ = bstack1l1lll1l1ll_opy_
                except Exception as e:
                    self.logger.error(bstack1ll11_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢ࡬ࡲࡻࡵ࡫ࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࠣ኷") + str(e) + bstack1ll11_opy_ (u"ࠦࠧኸ"))
                    traceback.print_exc()
            if bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.PRE and callable(bstack1l1llll1l11_opy_):
                return bstack1l1llll1l11_opy_
            elif bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.POST and bstack1l1llll1l11_opy_:
                return bstack1l1llll1l11_opy_
    def bstack1l1lll1llll_opy_(
        self, method_name, previous_state: bstack1lllllll1ll_opy_, *args, **kwargs
    ) -> bstack1lllllll1ll_opy_:
        if method_name == bstack1ll11_opy_ (u"ࠬࡲࡡࡶࡰࡦ࡬ࠬኹ") or method_name == bstack1ll11_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧኺ") or method_name == bstack1ll11_opy_ (u"ࠧ࡯ࡧࡺࡣࡵࡧࡧࡦࠩኻ"):
            return bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_
        if method_name == bstack1ll11_opy_ (u"ࠨࡦ࡬ࡷࡵࡧࡴࡤࡪࠪኼ"):
            return bstack1lllllll1ll_opy_.bstack1ll1lll1ll1_opy_
        if method_name == bstack1ll11_opy_ (u"ࠩࡦࡰࡴࡹࡥࠨኽ"):
            return bstack1lllllll1ll_opy_.QUIT
        return bstack1lllllll1ll_opy_.NONE
    @staticmethod
    def bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_]):
        return bstack1ll11_opy_ (u"ࠥ࠾ࠧኾ").join((bstack1lllllll1ll_opy_(bstack1llll1l1ll1_opy_[0]).name, bstack111111111l_opy_(bstack1llll1l1ll1_opy_[1]).name))
    @staticmethod
    def bstack11111111l1_opy_(bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_], callback: Callable):
        bstack1l1lll1l111_opy_ = bstack1llll1l11ll_opy_.bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_)
        if not bstack1l1lll1l111_opy_ in bstack1llll1l11ll_opy_.bstack1l1lll11l1l_opy_:
            bstack1llll1l11ll_opy_.bstack1l1lll11l1l_opy_[bstack1l1lll1l111_opy_] = []
        bstack1llll1l11ll_opy_.bstack1l1lll11l1l_opy_[bstack1l1lll1l111_opy_].append(callback)
    @staticmethod
    def bstack1l1lll1lll1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1lllll111l1_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll111l1_opy_(instance: bstack111111lll1_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1llll1l11ll_opy_.bstack1lll1l1lll1_opy_, default_value)
    @staticmethod
    def bstack1lll11l111l_opy_(instance: bstack111111lll1_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1111l_opy_(instance: bstack111111lll1_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1llll1l11ll_opy_.bstack1lll1l1l1ll_opy_, default_value)
    @staticmethod
    def bstack1l1lll11ll1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1llll1l11ll_opy_.bstack1l1lll1lll1_opy_(method_name):
            return False
        if not bstack1llll1l11ll_opy_.bstack1l1lll11lll_opy_ in bstack1llll1l11ll_opy_.bstack1lllll1ll11_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1llll1l11ll_opy_.bstack1l1lll11111_opy_(*args)
        return bstack1l1llll1111_opy_ and bstack1ll11_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦ኿") in bstack1l1llll1111_opy_ and bstack1ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨዀ") in bstack1l1llll1111_opy_[bstack1ll11_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨ዁")]
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str, *args):
        if not bstack1llll1l11ll_opy_.bstack1l1lll1lll1_opy_(method_name):
            return False
        if not bstack1llll1l11ll_opy_.bstack1l1lll11lll_opy_ in bstack1llll1l11ll_opy_.bstack1lllll1ll11_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1llll1l11ll_opy_.bstack1l1lll11111_opy_(*args)
        return (
            bstack1l1llll1111_opy_
            and bstack1ll11_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዂ") in bstack1l1llll1111_opy_
            and bstack1ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸࡩࡲࡪࡲࡷࠦዃ") in bstack1l1llll1111_opy_[bstack1ll11_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤዄ")]
        )
    @staticmethod
    def bstack1lllll1ll11_opy_(*args):
        return str(bstack1llll1l11ll_opy_.bstack1l1lll11ll1_opy_(*args)).lower()