# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1lll11ll1l1_opy_,
    bstack1111111l11_opy_,
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1l1ll11_opy_(bstack1lll11ll1l1_opy_):
    bstack1l1lll11111_opy_ = bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨኬ")
    bstack1llll1l1l11_opy_ = bstack1lllll1_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢክ")
    bstack1lll1l111l1_opy_ = bstack1lllll1_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭ࠤኮ")
    bstack1llll11l111_opy_ = bstack1lllll1_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣኯ")
    bstack1l1llll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࠨኰ")
    bstack1l1lll11lll_opy_ = bstack1lllll1_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࡡࡴࡻࡱࡧࠧ኱")
    NAME = bstack1lllll1_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤኲ")
    bstack1l1lll1l1l1_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack111111111l_opy_: Any
    bstack1l1lll1ll11_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1lllll1_opy_ (u"ࠨ࡬ࡢࡷࡱࡧ࡭ࠨኳ"), bstack1lllll1_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣኴ"), bstack1lllll1_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥኵ"), bstack1lllll1_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣ኶"), bstack1lllll1_opy_ (u"ࠥࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠧ኷")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1llll1ll1_opy_(methods)
    def bstack1l1llll11ll_opy_(self, instance: bstack1111111l11_opy_, method_name: str, bstack1l1lll1l11l_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1lll11l1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll1ll1l_opy_, bstack1l1llll111l_opy_ = bstack1lllll111ll_opy_
        bstack1l1llll1111_opy_ = bstack1lll1l1ll11_opy_.bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_)
        if bstack1l1llll1111_opy_ in bstack1lll1l1ll11_opy_.bstack1l1lll1l1l1_opy_:
            bstack1l1lll1111l_opy_ = None
            for callback in bstack1lll1l1ll11_opy_.bstack1l1lll1l1l1_opy_[bstack1l1llll1111_opy_]:
                try:
                    bstack1l1lll11ll1_opy_ = callback(self, target, exec, bstack1lllll111ll_opy_, result, *args, **kwargs)
                    if bstack1l1lll1111l_opy_ == None:
                        bstack1l1lll1111l_opy_ = bstack1l1lll11ll1_opy_
                except Exception as e:
                    self.logger.error(bstack1lllll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࠤኸ") + str(e) + bstack1lllll1_opy_ (u"ࠧࠨኹ"))
                    traceback.print_exc()
            if bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.PRE and callable(bstack1l1lll1111l_opy_):
                return bstack1l1lll1111l_opy_
            elif bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.POST and bstack1l1lll1111l_opy_:
                return bstack1l1lll1111l_opy_
    def bstack1l1llll11l1_opy_(
        self, method_name, previous_state: bstack1llll1ll1ll_opy_, *args, **kwargs
    ) -> bstack1llll1ll1ll_opy_:
        if method_name == bstack1lllll1_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࠭ኺ") or method_name == bstack1lllll1_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨኻ") or method_name == bstack1lllll1_opy_ (u"ࠨࡰࡨࡻࡤࡶࡡࡨࡧࠪኼ"):
            return bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_
        if method_name == bstack1lllll1_opy_ (u"ࠩࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠫኽ"):
            return bstack1llll1ll1ll_opy_.bstack1ll1llll1ll_opy_
        if method_name == bstack1lllll1_opy_ (u"ࠪࡧࡱࡵࡳࡦࠩኾ"):
            return bstack1llll1ll1ll_opy_.QUIT
        return bstack1llll1ll1ll_opy_.NONE
    @staticmethod
    def bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_]):
        return bstack1lllll1_opy_ (u"ࠦ࠿ࠨ኿").join((bstack1llll1ll1ll_opy_(bstack1lllll111ll_opy_[0]).name, bstack1lllll1lll1_opy_(bstack1lllll111ll_opy_[1]).name))
    @staticmethod
    def bstack11111111ll_opy_(bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_], callback: Callable):
        bstack1l1llll1111_opy_ = bstack1lll1l1ll11_opy_.bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_)
        if not bstack1l1llll1111_opy_ in bstack1lll1l1ll11_opy_.bstack1l1lll1l1l1_opy_:
            bstack1lll1l1ll11_opy_.bstack1l1lll1l1l1_opy_[bstack1l1llll1111_opy_] = []
        bstack1lll1l1ll11_opy_.bstack1l1lll1l1l1_opy_[bstack1l1llll1111_opy_].append(callback)
    @staticmethod
    def bstack1l1ll1lllll_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1llllll111l_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1111111l11_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lll1l1ll11_opy_.bstack1llll11l111_opy_, default_value)
    @staticmethod
    def bstack1lll11l1111_opy_(instance: bstack1111111l11_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1llll_opy_(instance: bstack1111111l11_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lll1l1ll11_opy_.bstack1lll1l111l1_opy_, default_value)
    @staticmethod
    def bstack1l1lll111l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1lll1l1ll11_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lll1l1ll11_opy_.bstack1l1llll1l1l_opy_ in bstack1lll1l1ll11_opy_.bstack1llllllllll_opy_(*args):
            return False
        bstack1l1llll1l11_opy_ = bstack1lll1l1ll11_opy_.bstack1l1lll1l111_opy_(*args)
        return bstack1l1llll1l11_opy_ and bstack1lllll1_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧዀ") in bstack1l1llll1l11_opy_ and bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢ዁") in bstack1l1llll1l11_opy_[bstack1lllll1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዂ")]
    @staticmethod
    def bstack1l1lll1l1ll_opy_(method_name: str, *args):
        if not bstack1lll1l1ll11_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lll1l1ll11_opy_.bstack1l1llll1l1l_opy_ in bstack1lll1l1ll11_opy_.bstack1llllllllll_opy_(*args):
            return False
        bstack1l1llll1l11_opy_ = bstack1lll1l1ll11_opy_.bstack1l1lll1l111_opy_(*args)
        return (
            bstack1l1llll1l11_opy_
            and bstack1lllll1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣዃ") in bstack1l1llll1l11_opy_
            and bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡣࡳ࡫ࡳࡸࠧዄ") in bstack1l1llll1l11_opy_[bstack1lllll1_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዅ")]
        )
    @staticmethod
    def bstack1llllllllll_opy_(*args):
        return str(bstack1lll1l1ll11_opy_.bstack1l1lll111l1_opy_(*args)).lower()