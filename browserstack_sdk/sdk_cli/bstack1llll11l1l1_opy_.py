# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import (
    bstack1lll11ll111_opy_,
    bstack1111111111_opy_,
    bstack1llll1l1lll_opy_,
    bstack1111111l1l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1ll11l1_opy_(bstack1lll11ll111_opy_):
    bstack1l1lll1l11l_opy_ = bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧኤ")
    bstack1lll1l11ll1_opy_ = bstack11l1l11_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨእ")
    bstack1lll1l1l11l_opy_ = bstack11l1l11_opy_ (u"ࠢࡩࡷࡥࡣࡺࡸ࡬ࠣኦ")
    bstack1lll1ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢኧ")
    bstack1l1lll1l1ll_opy_ = bstack11l1l11_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࠧከ")
    bstack1l1ll1lllll_opy_ = bstack11l1l11_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࡧࡳࡺࡰࡦࠦኩ")
    NAME = bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣኪ")
    bstack1l1lll1llll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llllll11ll_opy_: Any
    bstack1l1lll111ll_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11l1l11_opy_ (u"ࠧࡲࡡࡶࡰࡦ࡬ࠧካ"), bstack11l1l11_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢኬ"), bstack11l1l11_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤክ"), bstack11l1l11_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢኮ"), bstack11l1l11_opy_ (u"ࠤࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠦኯ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1llll111l_opy_(methods)
    def bstack1l1lll1111l_opy_(self, instance: bstack1111111111_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1llll11ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll1l1l_opy_, bstack1l1lll1l111_opy_ = bstack11111111l1_opy_
        bstack1l1lll1l1l1_opy_ = bstack1lll1ll11l1_opy_.bstack1l1llll1111_opy_(bstack11111111l1_opy_)
        if bstack1l1lll1l1l1_opy_ in bstack1lll1ll11l1_opy_.bstack1l1lll1llll_opy_:
            bstack1l1ll1llll1_opy_ = None
            for callback in bstack1lll1ll11l1_opy_.bstack1l1lll1llll_opy_[bstack1l1lll1l1l1_opy_]:
                try:
                    bstack1l1lll11ll1_opy_ = callback(self, target, exec, bstack11111111l1_opy_, result, *args, **kwargs)
                    if bstack1l1ll1llll1_opy_ == None:
                        bstack1l1ll1llll1_opy_ = bstack1l1lll11ll1_opy_
                except Exception as e:
                    self.logger.error(bstack11l1l11_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢ࡬ࡲࡻࡵ࡫ࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࠣኰ") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧ኱"))
                    traceback.print_exc()
            if bstack1l1lll1l111_opy_ == bstack1111111l1l_opy_.PRE and callable(bstack1l1ll1llll1_opy_):
                return bstack1l1ll1llll1_opy_
            elif bstack1l1lll1l111_opy_ == bstack1111111l1l_opy_.POST and bstack1l1ll1llll1_opy_:
                return bstack1l1ll1llll1_opy_
    def bstack1l1llll11l1_opy_(
        self, method_name, previous_state: bstack1llll1l1lll_opy_, *args, **kwargs
    ) -> bstack1llll1l1lll_opy_:
        if method_name == bstack11l1l11_opy_ (u"ࠬࡲࡡࡶࡰࡦ࡬ࠬኲ") or method_name == bstack11l1l11_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧኳ") or method_name == bstack11l1l11_opy_ (u"ࠧ࡯ࡧࡺࡣࡵࡧࡧࡦࠩኴ"):
            return bstack1llll1l1lll_opy_.bstack1111111lll_opy_
        if method_name == bstack11l1l11_opy_ (u"ࠨࡦ࡬ࡷࡵࡧࡴࡤࡪࠪኵ"):
            return bstack1llll1l1lll_opy_.bstack1ll1llll1ll_opy_
        if method_name == bstack11l1l11_opy_ (u"ࠩࡦࡰࡴࡹࡥࠨ኶"):
            return bstack1llll1l1lll_opy_.QUIT
        return bstack1llll1l1lll_opy_.NONE
    @staticmethod
    def bstack1l1llll1111_opy_(bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_]):
        return bstack11l1l11_opy_ (u"ࠥ࠾ࠧ኷").join((bstack1llll1l1lll_opy_(bstack11111111l1_opy_[0]).name, bstack1111111l1l_opy_(bstack11111111l1_opy_[1]).name))
    @staticmethod
    def bstack111111l11l_opy_(bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_], callback: Callable):
        bstack1l1lll1l1l1_opy_ = bstack1lll1ll11l1_opy_.bstack1l1llll1111_opy_(bstack11111111l1_opy_)
        if not bstack1l1lll1l1l1_opy_ in bstack1lll1ll11l1_opy_.bstack1l1lll1llll_opy_:
            bstack1lll1ll11l1_opy_.bstack1l1lll1llll_opy_[bstack1l1lll1l1l1_opy_] = []
        bstack1lll1ll11l1_opy_.bstack1l1lll1llll_opy_[bstack1l1lll1l1l1_opy_].append(callback)
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llll1lll1l_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll11lll_opy_(instance: bstack1111111111_opy_, default_value=None):
        return bstack1lll11ll111_opy_.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll1ll1l1l_opy_, default_value)
    @staticmethod
    def bstack1lll11l1lll_opy_(instance: bstack1111111111_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1lll1_opy_(instance: bstack1111111111_opy_, default_value=None):
        return bstack1lll11ll111_opy_.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1l1lll11l1l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1ll1l_opy_(method_name: str, *args):
        if not bstack1lll1ll11l1_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1lll1ll11l1_opy_.bstack1l1lll1l1ll_opy_ in bstack1lll1ll11l1_opy_.bstack1llll1lll11_opy_(*args):
            return False
        bstack1l1lll111l1_opy_ = bstack1lll1ll11l1_opy_.bstack1l1lll1ll11_opy_(*args)
        return bstack1l1lll111l1_opy_ and bstack11l1l11_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦኸ") in bstack1l1lll111l1_opy_ and bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨኹ") in bstack1l1lll111l1_opy_[bstack11l1l11_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨኺ")]
    @staticmethod
    def bstack1l1llll1l11_opy_(method_name: str, *args):
        if not bstack1lll1ll11l1_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1lll1ll11l1_opy_.bstack1l1lll1l1ll_opy_ in bstack1lll1ll11l1_opy_.bstack1llll1lll11_opy_(*args):
            return False
        bstack1l1lll111l1_opy_ = bstack1lll1ll11l1_opy_.bstack1l1lll1ll11_opy_(*args)
        return (
            bstack1l1lll111l1_opy_
            and bstack11l1l11_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢኻ") in bstack1l1lll111l1_opy_
            and bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸࡩࡲࡪࡲࡷࠦኼ") in bstack1l1lll111l1_opy_[bstack11l1l11_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤኽ")]
        )
    @staticmethod
    def bstack1llll1lll11_opy_(*args):
        return str(bstack1lll1ll11l1_opy_.bstack1l1lll11l1l_opy_(*args)).lower()