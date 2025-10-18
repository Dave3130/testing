# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lll1111ll1_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1lll1l111l1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
import weakref
class bstack1lll11lllll_opy_(bstack1lllllllll1_opy_):
    bstack1lll11ll111_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1lllll11l1l_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1lllll11l1l_opy_]]
    def __init__(self, bstack1lll11ll111_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1lllll1l_opy_ = dict()
        self.bstack1lll11ll111_opy_ = bstack1lll11ll111_opy_
        self.frameworks = frameworks
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1llll1_opy_, bstack1lllll1ll1l_opy_.POST), self.__1ll1lll1l1l_opy_)
        if any(bstack1lllll1l1l1_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_(
                (bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.PRE), self.__1ll1lllll11_opy_
            )
            bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_(
                (bstack1llll1ll1l1_opy_.QUIT, bstack1lllll1ll1l_opy_.POST), self.__1ll1llll111_opy_
            )
    def __1ll1lll1l1l_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1lll1lll_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11ll_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥᇕ"):
                return
            contexts = bstack1ll1lll1lll_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11ll_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢᇖ") in page.url:
                                self.logger.debug(bstack11ll_opy_ (u"ࠥࡗࡹࡵࡲࡪࡰࡪࠤࡹ࡮ࡥࠡࡰࡨࡻࠥࡶࡡࡨࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠧᇗ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll1111ll1_opy_.bstack1llllll1lll_opy_(instance, self.bstack1lll11ll111_opy_, True)
                                self.logger.debug(bstack11ll_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡳࡥ࡬࡫࡟ࡪࡰ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᇘ") + str(instance.ref()) + bstack11ll_opy_ (u"ࠧࠨᇙ"))
        except Exception as e:
            self.logger.debug(bstack11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦ࡮ࡦࡹࠣࡴࡦ࡭ࡥࠡ࠼ࠥᇚ"),e)
    def __1ll1lllll11_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll1111ll1_opy_.get_state(instance, self.bstack1lll11ll111_opy_, False):
            return
        if not f.bstack1ll1llll11l_opy_(f.hub_url(driver)):
            self.bstack1ll1lllll1l_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll1111ll1_opy_.bstack1llllll1lll_opy_(instance, self.bstack1lll11ll111_opy_, True)
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡪࡰ࡬ࡸ࠿ࠦ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᇛ") + str(instance.ref()) + bstack11ll_opy_ (u"ࠣࠤᇜ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll1111ll1_opy_.bstack1llllll1lll_opy_(instance, self.bstack1lll11ll111_opy_, True)
        self.logger.debug(bstack11ll_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᇝ") + str(instance.ref()) + bstack11ll_opy_ (u"ࠥࠦᇞ"))
    def __1ll1llll111_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1llll1ll_opy_(instance)
        self.logger.debug(bstack11ll_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡶࡻࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᇟ") + str(instance.ref()) + bstack11ll_opy_ (u"ࠧࠨᇠ"))
    def bstack1lll1llllll_opy_(self, context: bstack1lll1l111l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllll11l1l_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1llll1l1_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll1l1l1_opy_.bstack1lll111ll1l_opy_(data[1])
                    and data[1].bstack1ll1llll1l1_opy_(context)
                    and getattr(data[0](), bstack11ll_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᇡ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lllllll_opy_, reverse=reverse)
    def bstack1lll11lll11_opy_(self, context: bstack1lll1l111l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllll11l1l_opy_]]:
        matches = []
        for data in self.bstack1ll1lllll1l_opy_.values():
            if (
                data[1].bstack1ll1llll1l1_opy_(context)
                and getattr(data[0](), bstack11ll_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᇢ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lllllll_opy_, reverse=reverse)
    def bstack1ll1lll1ll1_opy_(self, instance: bstack1lllll11l1l_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1llll1ll_opy_(self, instance: bstack1lllll11l1l_opy_) -> bool:
        if self.bstack1ll1lll1ll1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll1111ll1_opy_.bstack1llllll1lll_opy_(instance, self.bstack1lll11ll111_opy_, False)
            return True
        return False