# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1lll11l1111_opy_,
    bstack1llll1l1111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll11ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1lll1lllll1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
import weakref
class bstack1lll1l111l1_opy_(bstack1llll1l1l11_opy_):
    bstack1llll11l111_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llll1l1111_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llll1l1111_opy_]]
    def __init__(self, bstack1llll11l111_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1lll1ll1_opy_ = dict()
        self.bstack1llll11l111_opy_ = bstack1llll11l111_opy_
        self.frameworks = frameworks
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llll11llll_opy_, bstack1llll1l1lll_opy_.POST), self.__1ll1lllll1l_opy_)
        if any(bstack1lllll11l1l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_(
                (bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.PRE), self.__1ll1llll11l_opy_
            )
            bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_(
                (bstack1lllll1lll1_opy_.QUIT, bstack1llll1l1lll_opy_.POST), self.__1ll1llllll1_opy_
            )
    def __1ll1lllll1l_opy_(
        self,
        f: bstack1lll11ll11l_opy_,
        bstack1lll1111111_opy_: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11l111_opy_ (u"ࠨ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠣᇓ"):
                return
            contexts = bstack1lll1111111_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11l111_opy_ (u"ࠢࡢࡤࡲࡹࡹࡀࡢ࡭ࡣࡱ࡯ࠧᇔ") in page.url:
                                self.logger.debug(bstack11l111_opy_ (u"ࠣࡕࡷࡳࡷ࡯࡮ࡨࠢࡷ࡬ࡪࠦ࡮ࡦࡹࠣࡴࡦ࡭ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠥᇕ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, self.bstack1llll11l111_opy_, True)
                                self.logger.debug(bstack11l111_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡱࡣࡪࡩࡤ࡯࡮ࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᇖ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠥࠦᇗ"))
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡲࡪࡰࡪࠤࡳ࡫ࡷࠡࡲࡤ࡫ࡪࠦ࠺ࠣᇘ"),e)
    def __1ll1llll11l_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll11l1111_opy_.get_state(instance, self.bstack1llll11l111_opy_, False):
            return
        if not f.bstack1ll1llll1l1_opy_(f.hub_url(driver)):
            self.bstack1ll1lll1ll1_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, self.bstack1llll11l111_opy_, True)
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤ࡯࡮ࡪࡶ࠽ࠤࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡥࡴ࡬ࡺࡪࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᇙ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠨࠢᇚ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, self.bstack1llll11l111_opy_, True)
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡪࡰ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᇛ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠣࠤᇜ"))
    def __1ll1llllll1_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1llll111_opy_(instance)
        self.logger.debug(bstack11l111_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡࡴࡹ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᇝ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠥࠦᇞ"))
    def bstack1lll11ll1l1_opy_(self, context: bstack1lll1lllll1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1l1111_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1llll1ll_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll11l1l_opy_.bstack1lll111l11l_opy_(data[1])
                    and data[1].bstack1ll1llll1ll_opy_(context)
                    and getattr(data[0](), bstack11l111_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣᇟ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lllll11_opy_, reverse=reverse)
    def bstack1lll1ll11ll_opy_(self, context: bstack1lll1lllll1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1l1111_opy_]]:
        matches = []
        for data in self.bstack1ll1lll1ll1_opy_.values():
            if (
                data[1].bstack1ll1llll1ll_opy_(context)
                and getattr(data[0](), bstack11l111_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᇠ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lllll11_opy_, reverse=reverse)
    def bstack1ll1lll1lll_opy_(self, instance: bstack1llll1l1111_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1llll111_opy_(self, instance: bstack1llll1l1111_opy_) -> bool:
        if self.bstack1ll1lll1lll_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, self.bstack1llll11l111_opy_, False)
            return True
        return False