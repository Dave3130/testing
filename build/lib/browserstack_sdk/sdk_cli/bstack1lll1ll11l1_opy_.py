# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1lll111llll_opy_,
    bstack111111l111_opy_,
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1llll11l1l1_opy_(bstack1lll111llll_opy_):
    bstack1l1lll111l1_opy_ = bstack1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣኮ")
    bstack1llll11lll1_opy_ = bstack1l_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤኯ")
    bstack1llll111ll1_opy_ = bstack1l_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦኰ")
    bstack1lll1llllll_opy_ = bstack1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥ኱")
    bstack1l1llll11ll_opy_ = bstack1l_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࠣኲ")
    bstack1l1lll11l11_opy_ = bstack1l_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࡣࡶࡽࡳࡩࠢኳ")
    NAME = bstack1l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦኴ")
    bstack1l1lll1llll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll1lll1_opy_: Any
    bstack1l1llll1l1l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1l_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣኵ"), bstack1l_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥ኶"), bstack1l_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧ኷"), bstack1l_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥኸ"), bstack1l_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢኹ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1l1lll1l111_opy_(methods)
    def bstack1l1ll1lllll_opy_(self, instance: bstack111111l111_opy_, method_name: str, bstack1l1lll1l1l1_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1l1lll1ll1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll1lll1_opy_, bstack1l1lll1l11l_opy_ = bstack1lllll1ll11_opy_
        bstack1l1llll1111_opy_ = bstack1llll11l1l1_opy_.bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_)
        if bstack1l1llll1111_opy_ in bstack1llll11l1l1_opy_.bstack1l1lll1llll_opy_:
            bstack1l1llll1l11_opy_ = None
            for callback in bstack1llll11l1l1_opy_.bstack1l1lll1llll_opy_[bstack1l1llll1111_opy_]:
                try:
                    bstack1l1lll11l1l_opy_ = callback(self, target, exec, bstack1lllll1ll11_opy_, result, *args, **kwargs)
                    if bstack1l1llll1l11_opy_ == None:
                        bstack1l1llll1l11_opy_ = bstack1l1lll11l1l_opy_
                except Exception as e:
                    self.logger.error(bstack1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࠦኺ") + str(e) + bstack1l_opy_ (u"ࠢࠣኻ"))
                    traceback.print_exc()
            if bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.PRE and callable(bstack1l1llll1l11_opy_):
                return bstack1l1llll1l11_opy_
            elif bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.POST and bstack1l1llll1l11_opy_:
                return bstack1l1llll1l11_opy_
    def bstack1l1lll111ll_opy_(
        self, method_name, previous_state: bstack1111111l11_opy_, *args, **kwargs
    ) -> bstack1111111l11_opy_:
        if method_name == bstack1l_opy_ (u"ࠨ࡮ࡤࡹࡳࡩࡨࠨኼ") or method_name == bstack1l_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࠪኽ") or method_name == bstack1l_opy_ (u"ࠪࡲࡪࡽ࡟ࡱࡣࡪࡩࠬኾ"):
            return bstack1111111l11_opy_.bstack1llllll1l1l_opy_
        if method_name == bstack1l_opy_ (u"ࠫࡩ࡯ࡳࡱࡣࡷࡧ࡭࠭኿"):
            return bstack1111111l11_opy_.bstack1ll1llll111_opy_
        if method_name == bstack1l_opy_ (u"ࠬࡩ࡬ࡰࡵࡨࠫዀ"):
            return bstack1111111l11_opy_.QUIT
        return bstack1111111l11_opy_.NONE
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_]):
        return bstack1l_opy_ (u"ࠨ࠺ࠣ዁").join((bstack1111111l11_opy_(bstack1lllll1ll11_opy_[0]).name, bstack1llllll1ll1_opy_(bstack1lllll1ll11_opy_[1]).name))
    @staticmethod
    def bstack1lllll1111l_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_], callback: Callable):
        bstack1l1llll1111_opy_ = bstack1llll11l1l1_opy_.bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_)
        if not bstack1l1llll1111_opy_ in bstack1llll11l1l1_opy_.bstack1l1lll1llll_opy_:
            bstack1llll11l1l1_opy_.bstack1l1lll1llll_opy_[bstack1l1llll1111_opy_] = []
        bstack1llll11l1l1_opy_.bstack1l1lll1llll_opy_[bstack1l1llll1111_opy_].append(callback)
    @staticmethod
    def bstack1l1lll11lll_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1lllll1llll_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1l1lll1l1ll_opy_(instance: bstack111111l111_opy_, default_value=None):
        return bstack1lll111llll_opy_.get_state(instance, bstack1llll11l1l1_opy_.bstack1lll1llllll_opy_, default_value)
    @staticmethod
    def bstack1lll11lll11_opy_(instance: bstack111111l111_opy_) -> bool:
        return True
    @staticmethod
    def bstack1l1llll1ll1_opy_(instance: bstack111111l111_opy_, default_value=None):
        return bstack1lll111llll_opy_.get_state(instance, bstack1llll11l1l1_opy_.bstack1llll111ll1_opy_, default_value)
    @staticmethod
    def bstack1l1llll11l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1llll111l_opy_(method_name: str, *args):
        if not bstack1llll11l1l1_opy_.bstack1l1lll11lll_opy_(method_name):
            return False
        if not bstack1llll11l1l1_opy_.bstack1l1llll11ll_opy_ in bstack1llll11l1l1_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll11111_opy_ = bstack1llll11l1l1_opy_.bstack1l1lll1ll11_opy_(*args)
        return bstack1l1lll11111_opy_ and bstack1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢዂ") in bstack1l1lll11111_opy_ and bstack1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤዃ") in bstack1l1lll11111_opy_[bstack1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤዄ")]
    @staticmethod
    def bstack1l1lll1111l_opy_(method_name: str, *args):
        if not bstack1llll11l1l1_opy_.bstack1l1lll11lll_opy_(method_name):
            return False
        if not bstack1llll11l1l1_opy_.bstack1l1llll11ll_opy_ in bstack1llll11l1l1_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll11111_opy_ = bstack1llll11l1l1_opy_.bstack1l1lll1ll11_opy_(*args)
        return (
            bstack1l1lll11111_opy_
            and bstack1l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥዅ") in bstack1l1lll11111_opy_
            and bstack1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡥࡵ࡭ࡵࡺࠢ዆") in bstack1l1lll11111_opy_[bstack1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧ዇")]
        )
    @staticmethod
    def bstack1llllll111l_opy_(*args):
        return str(bstack1llll11l1l1_opy_.bstack1l1llll11l1_opy_(*args)).lower()