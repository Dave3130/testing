# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1lllll11l11_opy_,
    bstack1llll1ll111_opy_,
)
from bstack_utils.helper import  bstack1l1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1llllll_opy_, bstack1lll1l1llll_opy_, bstack1lll1l1lll1_opy_, bstack1ll11111111_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l1ll11l1_opy_ import bstack11ll1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1lll11111l1_opy_
from bstack_utils.percy import bstack111l111ll_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1lll11l_opy_(bstack1lllll111l1_opy_):
    def __init__(self, bstack11lllll1l1l_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll1l1l_opy_ = bstack11lllll1l1l_opy_
        self.percy = bstack111l111ll_opy_()
        self.bstack1l11ll1l1l_opy_ = bstack11ll1l1111_opy_()
        self.bstack11llll1llll_opy_()
        bstack1lllllll1l1_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllllll11l_opy_, bstack1lllll11l11_opy_.PRE), self.bstack11llll1lll1_opy_)
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.POST), self.bstack1lll1l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11lll1_opy_(self, instance: bstack1llll1ll111_opy_, driver: object):
        bstack1l111llll1l_opy_ = TestFramework.bstack1l11l1ll11l_opy_(instance.context)
        for t in bstack1l111llll1l_opy_:
            bstack1lll11l1111_opy_ = TestFramework.get_state(t, bstack1lll11111l1_opy_.bstack1lll11llll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l1111_opy_) or instance == driver:
                return t
    def bstack11llll1lll1_opy_(
        self,
        f: bstack1lllllll1l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllllll1l1_opy_.bstack1l1lll11l1l_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllllll1l1_opy_.bstack1llll1l1l11_opy_, 0)
            bstack1ll111l11ll_opy_ = self.bstack1l11l11lll1_opy_(instance, driver)
            bstack11lllll11l1_opy_ = TestFramework.get_state(bstack1ll111l11ll_opy_, TestFramework.bstack1ll1111llll_opy_, None)
            if not bstack11lllll11l1_opy_:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡴࡨࡸࡺࡸ࡮ࡪࡰࡪࠤࡦࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡ࡫ࡶࠤࡳࡵࡴࠡࡻࡨࡸࠥࡹࡴࡢࡴࡷࡩࡩࠨᔷ"))
                return
            driver_command = f.bstack1l1ll1ll1ll_opy_(*args)
            for command in bstack111ll1ll11_opy_:
                if command == driver_command:
                    self.bstack11ll1lll1_opy_(driver, platform_index)
            bstack111l111l1_opy_ = self.percy.bstack11l111ll1_opy_()
            if driver_command in bstack11l11ll1l1_opy_[bstack111l111l1_opy_]:
                self.bstack1l11ll1l1l_opy_.bstack11llll1l11_opy_(bstack11lllll11l1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡨࡶࡷࡵࡲࠣᔸ"), e)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111llll1l_opy_ import bstack1llll11l1ll_opy_
        bstack1lll11l1111_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll11l1111_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᔹ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠤࠥᔺ"))
            return
        if len(bstack1lll11l1111_opy_) > 1:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔻ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠦࠧᔼ"))
        bstack1ll1lllllll_opy_, bstack1llll11111l_opy_ = bstack1lll11l1111_opy_[0]
        driver = bstack1ll1lllllll_opy_()
        if not driver:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔽ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠨࠢᔾ"))
            return
        bstack11lllll1111_opy_ = {
            TestFramework.bstack1ll11ll1lll_opy_: bstack1l111ll_opy_ (u"ࠢࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᔿ"),
            TestFramework.bstack1llll1111ll_opy_: bstack1l111ll_opy_ (u"ࠣࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᕀ"),
            TestFramework.bstack1ll1111llll_opy_: bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺࠠࡳࡧࡵࡹࡳࠦ࡮ࡢ࡯ࡨࠦᕁ")
        }
        bstack11lllll11ll_opy_ = { key: f.get_state(instance, key) for key in bstack11lllll1111_opy_ }
        bstack11llll1ll11_opy_ = [key for key, value in bstack11lllll11ll_opy_.items() if not value]
        if bstack11llll1ll11_opy_:
            for key in bstack11llll1ll11_opy_:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࠨᕂ") + str(key) + bstack1l111ll_opy_ (u"ࠦࠧᕃ"))
            return
        platform_index = f.get_state(instance, bstack1lllllll1l1_opy_.bstack1llll1l1l11_opy_, 0)
        if self.bstack11lllll1l1l_opy_.percy_capture_mode == bstack1l111ll_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕄ"):
            bstack1l1111111l_opy_ = bstack11lllll11ll_opy_.get(TestFramework.bstack1ll1111llll_opy_) + bstack1l111ll_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᕅ")
            bstack1ll111ll111_opy_ = bstack1llll11l1ll_opy_.bstack1ll1l11l1ll_opy_(EVENTS.bstack11lllll1l11_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l1111111l_opy_,
                bstack11l111llll_opy_=bstack11lllll11ll_opy_[TestFramework.bstack1ll11ll1lll_opy_],
                bstack1l111l1lll_opy_=bstack11lllll11ll_opy_[TestFramework.bstack1llll1111ll_opy_],
                bstack1l11ll1ll_opy_=platform_index
            )
            bstack1llll11l1ll_opy_.end(EVENTS.bstack11lllll1l11_opy_.value, bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᕆ"), bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᕇ"), True, None, None, None, None, test_name=bstack1l1111111l_opy_)
    def bstack11ll1lll1_opy_(self, driver, platform_index):
        if self.bstack1l11ll1l1l_opy_.bstack111l111l11_opy_() is True or self.bstack1l11ll1l1l_opy_.capturing() is True:
            return
        self.bstack1l11ll1l1l_opy_.bstack11llll1ll_opy_()
        while not self.bstack1l11ll1l1l_opy_.bstack111l111l11_opy_():
            bstack11lllll11l1_opy_ = self.bstack1l11ll1l1l_opy_.bstack1l1l11lll1_opy_()
            self.bstack1ll111ll11_opy_(driver, bstack11lllll11l1_opy_, platform_index)
        self.bstack1l11ll1l1l_opy_.bstack11ll1lllll_opy_()
    def bstack1ll111ll11_opy_(self, driver, bstack1l1lllll1_opy_, platform_index, test=None):
        from bstack_utils.bstack111llll1l_opy_ import bstack1llll11l1ll_opy_
        bstack1ll111ll111_opy_ = bstack1llll11l1ll_opy_.bstack1ll1l11l1ll_opy_(EVENTS.bstack11ll1l1ll_opy_.value)
        if test != None:
            bstack11l111llll_opy_ = getattr(test, bstack1l111ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᕈ"), None)
            bstack1l111l1lll_opy_ = getattr(test, bstack1l111ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᕉ"), None)
            PercySDK.screenshot(driver, bstack1l1lllll1_opy_, bstack11l111llll_opy_=bstack11l111llll_opy_, bstack1l111l1lll_opy_=bstack1l111l1lll_opy_, bstack1l11ll1ll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l1lllll1_opy_)
        bstack1llll11l1ll_opy_.end(EVENTS.bstack11ll1l1ll_opy_.value, bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕊ"), bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕋ"), True, None, None, None, None, test_name=bstack1l1lllll1_opy_)
    def bstack11llll1llll_opy_(self):
        os.environ[bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᕌ")] = str(self.bstack11lllll1l1l_opy_.success)
        os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᕍ")] = str(self.bstack11lllll1l1l_opy_.percy_capture_mode)
        self.percy.bstack11llll1ll1l_opy_(self.bstack11lllll1l1l_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll111l_opy_(self.bstack11lllll1l1l_opy_.percy_build_id)