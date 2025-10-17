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
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1llll1l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import (
    bstack1lllll11111_opy_,
    bstack1llllllll1l_opy_,
    bstack1lll11ll11l_opy_,
    bstack1llllll1lll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1ll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111l11_opy_ import bstack1lll1lll1l1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1llll1l1l1l_opy_
import weakref
class bstack1lll1llllll_opy_(bstack1llll1l1l1l_opy_):
    bstack1llll11l1l1_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llllll1lll_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llllll1lll_opy_]]
    def __init__(self, bstack1llll11l1l1_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll11111ll_opy_ = dict()
        self.bstack1llll11l1l1_opy_ = bstack1llll11l1l1_opy_
        self.frameworks = frameworks
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1lllll11lll_opy_, bstack1llllllll1l_opy_.POST), self.__1ll1lllllll_opy_)
        if any(bstack1lllllll1ll_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllllll1ll_opy_.bstack1llll1llll1_opy_(
                (bstack1lllll11111_opy_.bstack1llll1lllll_opy_, bstack1llllllll1l_opy_.PRE), self.__1lll1111111_opy_
            )
            bstack1lllllll1ll_opy_.bstack1llll1llll1_opy_(
                (bstack1lllll11111_opy_.QUIT, bstack1llllllll1l_opy_.POST), self.__1lll1111lll_opy_
            )
    def __1ll1lllllll_opy_(
        self,
        f: bstack1lll1ll1ll1_opy_,
        bstack1lll1111l1l_opy_: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11l111_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨᆠ"):
                return
            contexts = bstack1lll1111l1l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11l111_opy_ (u"ࠧࡧࡢࡰࡷࡷ࠾ࡧࡲࡡ࡯࡭ࠥᆡ") in page.url:
                                self.logger.debug(bstack11l111_opy_ (u"ࠨࡓࡵࡱࡵ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡳ࡫ࡷࠡࡲࡤ࡫ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠣᆢ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll11ll11l_opy_.bstack1lllll111ll_opy_(instance, self.bstack1llll11l1l1_opy_, True)
                                self.logger.debug(bstack11l111_opy_ (u"ࠢࡠࡡࡲࡲࡤࡶࡡࡨࡧࡢ࡭ࡳ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᆣ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠣࠤᆤ"))
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡱࡩࡼࠦࡰࡢࡩࡨࠤ࠿ࠨᆥ"),e)
    def __1lll1111111_opy_(
        self,
        f: bstack1lllllll1ll_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll11ll11l_opy_.get_state(instance, self.bstack1llll11l1l1_opy_, False):
            return
        if not f.bstack1lll11111l1_opy_(f.hub_url(driver)):
            self.bstack1lll11111ll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll11ll11l_opy_.bstack1lllll111ll_opy_(instance, self.bstack1llll11l1l1_opy_, True)
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡭ࡳ࡯ࡴ࠻ࠢࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᆦ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠦࠧᆧ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll11ll11l_opy_.bstack1lllll111ll_opy_(instance, self.bstack1llll11l1l1_opy_, True)
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤ࡯࡮ࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᆨ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠨࠢᆩ"))
    def __1lll1111lll_opy_(
        self,
        f: bstack1lllllll1ll_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll111111l_opy_(instance)
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡲࡷ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᆪ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠣࠤᆫ"))
    def bstack1llll11111l_opy_(self, context: bstack1lll1lll1l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllll1lll_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll1111ll1_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllllll1ll_opy_.bstack1lll11ll1l1_opy_(data[1])
                    and data[1].bstack1lll1111ll1_opy_(context)
                    and getattr(data[0](), bstack11l111_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᆬ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1llllll1_opy_, reverse=reverse)
    def bstack1lll1l1ll11_opy_(self, context: bstack1lll1lll1l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllll1lll_opy_]]:
        matches = []
        for data in self.bstack1lll11111ll_opy_.values():
            if (
                data[1].bstack1lll1111ll1_opy_(context)
                and getattr(data[0](), bstack11l111_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᆭ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1llllll1_opy_, reverse=reverse)
    def bstack1ll1lllll1l_opy_(self, instance: bstack1llllll1lll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll111111l_opy_(self, instance: bstack1llllll1lll_opy_) -> bool:
        if self.bstack1ll1lllll1l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll11ll11l_opy_.bstack1lllll111ll_opy_(instance, self.bstack1llll11l1l1_opy_, False)
            return True
        return False