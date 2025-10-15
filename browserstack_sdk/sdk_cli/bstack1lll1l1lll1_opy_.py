# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lll11l1111_opy_,
    bstack1llllllll1l_opy_,
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1l1ll11_opy_(bstack1lll11l1111_opy_):
    bstack1l1lll1ll1l_opy_ = bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢኦ")
    bstack1lll1l1llll_opy_ = bstack1ll1l_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣኧ")
    bstack1llll11l11l_opy_ = bstack1ll1l_opy_ (u"ࠤ࡫ࡹࡧࡥࡵࡳ࡮ࠥከ")
    bstack1lll1l1111l_opy_ = bstack1ll1l_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤኩ")
    bstack1l1lll111l1_opy_ = bstack1ll1l_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࠢኪ")
    bstack1l1llll1l11_opy_ = bstack1ll1l_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࡢࡵࡼࡲࡨࠨካ")
    NAME = bstack1ll1l_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥኬ")
    bstack1l1llll11l1_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1l11ll_opy_: Any
    bstack1l1lll11l1l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1ll1l_opy_ (u"ࠢ࡭ࡣࡸࡲࡨ࡮ࠢክ"), bstack1ll1l_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤኮ"), bstack1ll1l_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦኯ"), bstack1ll1l_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤኰ"), bstack1ll1l_opy_ (u"ࠦࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠨ኱")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1lll111ll_opy_(methods)
    def bstack1l1lll1111l_opy_(self, instance: bstack1llllllll1l_opy_, method_name: str, bstack1l1lll1ll11_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1llll11ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll11ll1_opy_, bstack1l1lll1llll_opy_ = bstack1llllll111l_opy_
        bstack1l1ll1lllll_opy_ = bstack1lll1l1ll11_opy_.bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_)
        if bstack1l1ll1lllll_opy_ in bstack1lll1l1ll11_opy_.bstack1l1llll11l1_opy_:
            bstack1l1ll1llll1_opy_ = None
            for callback in bstack1lll1l1ll11_opy_.bstack1l1llll11l1_opy_[bstack1l1ll1lllll_opy_]:
                try:
                    bstack1l1lll11l11_opy_ = callback(self, target, exec, bstack1llllll111l_opy_, result, *args, **kwargs)
                    if bstack1l1ll1llll1_opy_ == None:
                        bstack1l1ll1llll1_opy_ = bstack1l1lll11l11_opy_
                except Exception as e:
                    self.logger.error(bstack1ll1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࠥኲ") + str(e) + bstack1ll1l_opy_ (u"ࠨࠢኳ"))
                    traceback.print_exc()
            if bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.PRE and callable(bstack1l1ll1llll1_opy_):
                return bstack1l1ll1llll1_opy_
            elif bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.POST and bstack1l1ll1llll1_opy_:
                return bstack1l1ll1llll1_opy_
    def bstack1l1lll11lll_opy_(
        self, method_name, previous_state: bstack1lllll11l1l_opy_, *args, **kwargs
    ) -> bstack1lllll11l1l_opy_:
        if method_name == bstack1ll1l_opy_ (u"ࠧ࡭ࡣࡸࡲࡨ࡮ࠧኴ") or method_name == bstack1ll1l_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࠩኵ") or method_name == bstack1ll1l_opy_ (u"ࠩࡱࡩࡼࡥࡰࡢࡩࡨࠫ኶"):
            return bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_
        if method_name == bstack1ll1l_opy_ (u"ࠪࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠬ኷"):
            return bstack1lllll11l1l_opy_.bstack1ll1lll1l11_opy_
        if method_name == bstack1ll1l_opy_ (u"ࠫࡨࡲ࡯ࡴࡧࠪኸ"):
            return bstack1lllll11l1l_opy_.QUIT
        return bstack1lllll11l1l_opy_.NONE
    @staticmethod
    def bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_]):
        return bstack1ll1l_opy_ (u"ࠧࡀࠢኹ").join((bstack1lllll11l1l_opy_(bstack1llllll111l_opy_[0]).name, bstack1111111lll_opy_(bstack1llllll111l_opy_[1]).name))
    @staticmethod
    def bstack1lllll1l11l_opy_(bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_], callback: Callable):
        bstack1l1ll1lllll_opy_ = bstack1lll1l1ll11_opy_.bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_)
        if not bstack1l1ll1lllll_opy_ in bstack1lll1l1ll11_opy_.bstack1l1llll11l1_opy_:
            bstack1lll1l1ll11_opy_.bstack1l1llll11l1_opy_[bstack1l1ll1lllll_opy_] = []
        bstack1lll1l1ll11_opy_.bstack1l1llll11l1_opy_[bstack1l1ll1lllll_opy_].append(callback)
    @staticmethod
    def bstack1l1lll1l1ll_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1lllll1111l_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1lll1_opy_(instance: bstack1llllllll1l_opy_, default_value=None):
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lll1l1ll11_opy_.bstack1lll1l1111l_opy_, default_value)
    @staticmethod
    def bstack1lll111ll1l_opy_(instance: bstack1llllllll1l_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll11111_opy_(instance: bstack1llllllll1l_opy_, default_value=None):
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lll1l1ll11_opy_.bstack1llll11l11l_opy_, default_value)
    @staticmethod
    def bstack1l1lll1l11l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1l111_opy_(method_name: str, *args):
        if not bstack1lll1l1ll11_opy_.bstack1l1lll1l1ll_opy_(method_name):
            return False
        if not bstack1lll1l1ll11_opy_.bstack1l1lll111l1_opy_ in bstack1lll1l1ll11_opy_.bstack1111111l1l_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1lll1l1ll11_opy_.bstack1l1llll111l_opy_(*args)
        return bstack1l1llll1111_opy_ and bstack1ll1l_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨኺ") in bstack1l1llll1111_opy_ and bstack1ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣኻ") in bstack1l1llll1111_opy_[bstack1ll1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣኼ")]
    @staticmethod
    def bstack1l1lll1l1l1_opy_(method_name: str, *args):
        if not bstack1lll1l1ll11_opy_.bstack1l1lll1l1ll_opy_(method_name):
            return False
        if not bstack1lll1l1ll11_opy_.bstack1l1lll111l1_opy_ in bstack1lll1l1ll11_opy_.bstack1111111l1l_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1lll1l1ll11_opy_.bstack1l1llll111l_opy_(*args)
        return (
            bstack1l1llll1111_opy_
            and bstack1ll1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤኽ") in bstack1l1llll1111_opy_
            and bstack1ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡤࡴ࡬ࡴࡹࠨኾ") in bstack1l1llll1111_opy_[bstack1ll1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦ኿")]
        )
    @staticmethod
    def bstack1111111l1l_opy_(*args):
        return str(bstack1lll1l1ll11_opy_.bstack1l1lll1l11l_opy_(*args)).lower()