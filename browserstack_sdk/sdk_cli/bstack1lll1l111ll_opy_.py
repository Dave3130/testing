# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import (
    bstack1lll11ll11l_opy_,
    bstack1llllll1lll_opy_,
    bstack1lllll11111_opy_,
    bstack1llllllll1l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1ll1ll1_opy_(bstack1lll11ll11l_opy_):
    bstack1l1lll1ll1l_opy_ = bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥኛ")
    bstack1llll111l11_opy_ = bstack11l111_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦኜ")
    bstack1lll1l1l11l_opy_ = bstack11l111_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࠨኝ")
    bstack1lll1l1llll_opy_ = bstack11l111_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧኞ")
    bstack1l1lll11lll_opy_ = bstack11l111_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥኟ")
    bstack1l1ll1llll1_opy_ = bstack11l111_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤአ")
    NAME = bstack11l111_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨኡ")
    bstack1l1lll1111l_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll1llll_opy_: Any
    bstack1l1lll1l1l1_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11l111_opy_ (u"ࠥࡰࡦࡻ࡮ࡤࡪࠥኢ"), bstack11l111_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࠧኣ"), bstack11l111_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢኤ"), bstack11l111_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧእ"), bstack11l111_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤኦ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1ll1lllll_opy_(methods)
    def bstack1l1ll1ll1ll_opy_(self, instance: bstack1llllll1lll_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1lll1l111_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll1111_opy_, bstack1l1llll111l_opy_ = bstack1llll1ll1ll_opy_
        bstack1l1lll1llll_opy_ = bstack1lll1ll1ll1_opy_.bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_)
        if bstack1l1lll1llll_opy_ in bstack1lll1ll1ll1_opy_.bstack1l1lll1111l_opy_:
            bstack1l1lll1l1ll_opy_ = None
            for callback in bstack1lll1ll1ll1_opy_.bstack1l1lll1111l_opy_[bstack1l1lll1llll_opy_]:
                try:
                    bstack1l1lll111l1_opy_ = callback(self, target, exec, bstack1llll1ll1ll_opy_, result, *args, **kwargs)
                    if bstack1l1lll1l1ll_opy_ == None:
                        bstack1l1lll1l1ll_opy_ = bstack1l1lll111l1_opy_
                except Exception as e:
                    self.logger.error(bstack11l111_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨኧ") + str(e) + bstack11l111_opy_ (u"ࠤࠥከ"))
                    traceback.print_exc()
            if bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.PRE and callable(bstack1l1lll1l1ll_opy_):
                return bstack1l1lll1l1ll_opy_
            elif bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.POST and bstack1l1lll1l1ll_opy_:
                return bstack1l1lll1l1ll_opy_
    def bstack1l1lll1ll11_opy_(
        self, method_name, previous_state: bstack1lllll11111_opy_, *args, **kwargs
    ) -> bstack1lllll11111_opy_:
        if method_name == bstack11l111_opy_ (u"ࠪࡰࡦࡻ࡮ࡤࡪࠪኩ") or method_name == bstack11l111_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࠬኪ") or method_name == bstack11l111_opy_ (u"ࠬࡴࡥࡸࡡࡳࡥ࡬࡫ࠧካ"):
            return bstack1lllll11111_opy_.bstack1lllll11lll_opy_
        if method_name == bstack11l111_opy_ (u"࠭ࡤࡪࡵࡳࡥࡹࡩࡨࠨኬ"):
            return bstack1lllll11111_opy_.bstack1ll1ll1llll_opy_
        if method_name == bstack11l111_opy_ (u"ࠧࡤ࡮ࡲࡷࡪ࠭ክ"):
            return bstack1lllll11111_opy_.QUIT
        return bstack1lllll11111_opy_.NONE
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_]):
        return bstack11l111_opy_ (u"ࠣ࠼ࠥኮ").join((bstack1lllll11111_opy_(bstack1llll1ll1ll_opy_[0]).name, bstack1llllllll1l_opy_(bstack1llll1ll1ll_opy_[1]).name))
    @staticmethod
    def bstack1llll1llll1_opy_(bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_], callback: Callable):
        bstack1l1lll1llll_opy_ = bstack1lll1ll1ll1_opy_.bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_)
        if not bstack1l1lll1llll_opy_ in bstack1lll1ll1ll1_opy_.bstack1l1lll1111l_opy_:
            bstack1lll1ll1ll1_opy_.bstack1l1lll1111l_opy_[bstack1l1lll1llll_opy_] = []
        bstack1lll1ll1ll1_opy_.bstack1l1lll1111l_opy_[bstack1l1lll1llll_opy_].append(callback)
    @staticmethod
    def bstack1l1ll1lll11_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1111111ll1_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1lll1_opy_(instance: bstack1llllll1lll_opy_, default_value=None):
        return bstack1lll11ll11l_opy_.get_state(instance, bstack1lll1ll1ll1_opy_.bstack1lll1l1llll_opy_, default_value)
    @staticmethod
    def bstack1lll11ll1l1_opy_(instance: bstack1llllll1lll_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1llllll1lll_opy_, default_value=None):
        return bstack1lll11ll11l_opy_.get_state(instance, bstack1lll1ll1ll1_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1l1llll11l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll11l1l_opy_(method_name: str, *args):
        if not bstack1lll1ll1ll1_opy_.bstack1l1ll1lll11_opy_(method_name):
            return False
        if not bstack1lll1ll1ll1_opy_.bstack1l1lll11lll_opy_ in bstack1lll1ll1ll1_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll111ll_opy_ = bstack1lll1ll1ll1_opy_.bstack1l1ll1lll1l_opy_(*args)
        return bstack1l1lll111ll_opy_ and bstack11l111_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤኯ") in bstack1l1lll111ll_opy_ and bstack11l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦኰ") in bstack1l1lll111ll_opy_[bstack11l111_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦ኱")]
    @staticmethod
    def bstack1l1lll1l11l_opy_(method_name: str, *args):
        if not bstack1lll1ll1ll1_opy_.bstack1l1ll1lll11_opy_(method_name):
            return False
        if not bstack1lll1ll1ll1_opy_.bstack1l1lll11lll_opy_ in bstack1lll1ll1ll1_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll111ll_opy_ = bstack1lll1ll1ll1_opy_.bstack1l1ll1lll1l_opy_(*args)
        return (
            bstack1l1lll111ll_opy_
            and bstack11l111_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧኲ") in bstack1l1lll111ll_opy_
            and bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤኳ") in bstack1l1lll111ll_opy_[bstack11l111_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢኴ")]
        )
    @staticmethod
    def bstack1llllll111l_opy_(*args):
        return str(bstack1lll1ll1ll1_opy_.bstack1l1llll11l1_opy_(*args)).lower()