# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lll111lll1_opy_,
    bstack1lllllll11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1lll111_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1lll1l1lll1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
import weakref
class bstack1lll1llllll_opy_(bstack1lllllll1l1_opy_):
    bstack1lll1ll1111_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1lllllll11l_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1lllllll11l_opy_]]
    def __init__(self, bstack1lll1ll1111_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1lllll11_opy_ = dict()
        self.bstack1lll1ll1111_opy_ = bstack1lll1ll1111_opy_
        self.frameworks = frameworks
        bstack1lll1lll111_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1l1ll1_opy_, bstack1llll1lllll_opy_.POST), self.__1ll1llll11l_opy_)
        if any(bstack1llllll1ll1_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1llllll1ll1_opy_.bstack1lllll11111_opy_(
                (bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.PRE), self.__1ll1lll1l1l_opy_
            )
            bstack1llllll1ll1_opy_.bstack1lllll11111_opy_(
                (bstack1111111111_opy_.QUIT, bstack1llll1lllll_opy_.POST), self.__1ll1lll1ll1_opy_
            )
    def __1ll1llll11l_opy_(
        self,
        f: bstack1lll1lll111_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1lll11l_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨᇊ"):
                return
            contexts = bstack1ll1llll111_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1lll11l_opy_ (u"ࠧࡧࡢࡰࡷࡷ࠾ࡧࡲࡡ࡯࡭ࠥᇋ") in page.url:
                                self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡓࡵࡱࡵ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡳ࡫ࡷࠡࡲࡤ࡫ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠣᇌ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, self.bstack1lll1ll1111_opy_, True)
                                self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡠࡡࡲࡲࡤࡶࡡࡨࡧࡢ࡭ࡳ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᇍ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠣࠤᇎ"))
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡱࡩࡼࠦࡰࡢࡩࡨࠤ࠿ࠨᇏ"),e)
    def __1ll1lll1l1l_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111lll1_opy_.get_state(instance, self.bstack1lll1ll1111_opy_, False):
            return
        if not f.bstack1ll1lllll1l_opy_(f.hub_url(driver)):
            self.bstack1ll1lllll11_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, self.bstack1lll1ll1111_opy_, True)
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡭ࡳ࡯ࡴ࠻ࠢࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᇐ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠦࠧᇑ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, self.bstack1lll1ll1111_opy_, True)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤ࡯࡮ࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᇒ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠨࠢᇓ"))
    def __1ll1lll1ll1_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1lllllll_opy_(instance)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡲࡷ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᇔ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠣࠤᇕ"))
    def bstack1lll1ll1lll_opy_(self, context: bstack1lll1l1lll1_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllllll11l_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1lll1lll_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1llllll1ll1_opy_.bstack1lll1111ll1_opy_(data[1])
                    and data[1].bstack1ll1lll1lll_opy_(context)
                    and getattr(data[0](), bstack1lll11l_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᇖ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1llll1l1_opy_, reverse=reverse)
    def bstack1lll1ll11ll_opy_(self, context: bstack1lll1l1lll1_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllllll11l_opy_]]:
        matches = []
        for data in self.bstack1ll1lllll11_opy_.values():
            if (
                data[1].bstack1ll1lll1lll_opy_(context)
                and getattr(data[0](), bstack1lll11l_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᇗ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1llll1l1_opy_, reverse=reverse)
    def bstack1ll1llll1ll_opy_(self, instance: bstack1lllllll11l_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1lllllll_opy_(self, instance: bstack1lllllll11l_opy_) -> bool:
        if self.bstack1ll1llll1ll_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, self.bstack1lll1ll1111_opy_, False)
            return True
        return False