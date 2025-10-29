# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import (
    bstack1lllll1l1ll_opy_,
    bstack1llllll11ll_opy_,
    bstack1ll1llllll1_opy_,
    bstack1llll1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1lll1_opy_ import bstack1lll1l111l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1lll1l1l1ll_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
import weakref
class bstack1lll11ll1ll_opy_(bstack1lllll11111_opy_):
    bstack1lll1ll1111_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llll1llll1_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llll1llll1_opy_]]
    def __init__(self, bstack1lll1ll1111_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1lllll11_opy_ = dict()
        self.bstack1lll1ll1111_opy_ = bstack1lll1ll1111_opy_
        self.frameworks = frameworks
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_, bstack1llllll11ll_opy_.POST), self.__1ll1lll1lll_opy_)
        if any(bstack1llll1l111l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_(
                (bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, bstack1llllll11ll_opy_.PRE), self.__1ll1lll11l1_opy_
            )
            bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_(
                (bstack1lllll1l1ll_opy_.QUIT, bstack1llllll11ll_opy_.POST), self.__1ll1llll1ll_opy_
            )
    def __1ll1lll1lll_opy_(
        self,
        f: bstack1lll1l111l1_opy_,
        bstack1ll1llll11l_opy_: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11l11ll_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᇠ"):
                return
            contexts = bstack1ll1llll11l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11l11ll_opy_ (u"ࠨࡡࡣࡱࡸࡸ࠿ࡨ࡬ࡢࡰ࡮ࠦᇡ") in page.url:
                                self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡔࡶࡲࡶ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡴࡥࡸࠢࡳࡥ࡬࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠤᇢ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1ll1llllll1_opy_.bstack1llll1l1l11_opy_(instance, self.bstack1lll1ll1111_opy_, True)
                                self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡡࡢࡳࡳࡥࡰࡢࡩࡨࡣ࡮ࡴࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᇣ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠤࠥᇤ"))
        except Exception as e:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡲࡪࡽࠠࡱࡣࡪࡩࠥࡀࠢᇥ"),e)
    def __1ll1lll11l1_opy_(
        self,
        f: bstack1llll1l111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1ll1llllll1_opy_.get_state(instance, self.bstack1lll1ll1111_opy_, False):
            return
        if not f.bstack1ll1llll1l1_opy_(f.hub_url(driver)):
            self.bstack1ll1lllll11_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1ll1llllll1_opy_.bstack1llll1l1l11_opy_(instance, self.bstack1lll1ll1111_opy_, True)
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣ࡮ࡴࡩࡵ࠼ࠣࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᇦ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠧࠨᇧ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1ll1llllll1_opy_.bstack1llll1l1l11_opy_(instance, self.bstack1lll1ll1111_opy_, True)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡩ࡯࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᇨ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠢࠣᇩ"))
    def __1ll1llll1ll_opy_(
        self,
        f: bstack1llll1l111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1lll11ll_opy_(instance)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡳࡸ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᇪ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠤࠥᇫ"))
    def bstack1lll11lllll_opy_(self, context: bstack1lll1l1l1ll_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1llll1_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1llll111_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1llll1l111l_opy_.bstack1lll111111l_opy_(data[1])
                    and data[1].bstack1ll1llll111_opy_(context)
                    and getattr(data[0](), bstack11l11ll_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᇬ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lll1l11_opy_, reverse=reverse)
    def bstack1lll1lll1ll_opy_(self, context: bstack1lll1l1l1ll_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1llll1_opy_]]:
        matches = []
        for data in self.bstack1ll1lllll11_opy_.values():
            if (
                data[1].bstack1ll1llll111_opy_(context)
                and getattr(data[0](), bstack11l11ll_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣᇭ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lll1l11_opy_, reverse=reverse)
    def bstack1ll1lll1ll1_opy_(self, instance: bstack1llll1llll1_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1lll11ll_opy_(self, instance: bstack1llll1llll1_opy_) -> bool:
        if self.bstack1ll1lll1ll1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1ll1llllll1_opy_.bstack1llll1l1l11_opy_(instance, self.bstack1lll1ll1111_opy_, False)
            return True
        return False