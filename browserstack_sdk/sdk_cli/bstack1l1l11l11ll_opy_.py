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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1llll1l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import (
    bstack1lllll11111_opy_,
    bstack1llllllll1l_opy_,
    bstack1llllll1lll_opy_,
)
from bstack_utils.helper import  bstack1l11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllll1ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1l1ll_opy_, bstack1lll1ll1lll_opy_, bstack1lll1ll11ll_opy_, bstack1ll1111lll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1llll1l1ll_opy_ import bstack1l1llll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111lll1_opy_ import bstack1lll11l1l11_opy_
from bstack_utils.percy import bstack1ll1l1ll1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l11ll111_opy_(bstack1llll1l1l1l_opy_):
    def __init__(self, bstack11lllll1lll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll1lll_opy_ = bstack11lllll1lll_opy_
        self.percy = bstack1ll1l1ll1l_opy_()
        self.bstack11l1l1ll11_opy_ = bstack1l1llll11l_opy_()
        self.bstack11lllll1ll1_opy_()
        bstack1lllllll1ll_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1llll1lllll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack11llllll1ll_opy_)
        TestFramework.bstack1llll1llll1_opy_((bstack1lll1l1l1ll_opy_.TEST, bstack1lll1ll11ll_opy_.POST), self.bstack1lll1lll111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1l111l_opy_(self, instance: bstack1llllll1lll_opy_, driver: object):
        bstack1l11l11lll1_opy_ = TestFramework.bstack1l11l11l1ll_opy_(instance.context)
        for t in bstack1l11l11lll1_opy_:
            bstack1lll11l11l1_opy_ = TestFramework.get_state(t, bstack1lll11l1l11_opy_.bstack1llll11lll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l11l1_opy_) or instance == driver:
                return t
    def bstack11llllll1ll_opy_(
        self,
        f: bstack1lllllll1ll_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllllll1ll_opy_.bstack1l1ll1lll11_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllllll1ll_opy_.bstack1111111l1l_opy_, 0)
            bstack1ll1l111111_opy_ = self.bstack1l11l1l111l_opy_(instance, driver)
            bstack11llllll11l_opy_ = TestFramework.get_state(bstack1ll1l111111_opy_, TestFramework.bstack1ll11ll1lll_opy_, None)
            if not bstack11llllll11l_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡷ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡢࡵࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡾ࡫ࡴࠡࡵࡷࡥࡷࡺࡥࡥࠤᔉ"))
                return
            driver_command = f.bstack1l1llll11l1_opy_(*args)
            for command in bstack1l1l1l11ll_opy_:
                if command == driver_command:
                    self.bstack11ll11111l_opy_(driver, platform_index)
            bstack11lll11ll_opy_ = self.percy.bstack11l11l1ll_opy_()
            if driver_command in bstack1ll1111ll1_opy_[bstack11lll11ll_opy_]:
                self.bstack11l1l1ll11_opy_.bstack1ll11ll1l1_opy_(bstack11llllll11l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥ࡫ࡲࡳࡱࡵࠦᔊ"), e)
    def bstack1lll1lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1lll_opy_,
        bstack1llll1ll1ll_opy_: Tuple[bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1l11_opy_.bstack1llll11lll1_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔋ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᔌ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(bstack11l111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᔍ") + str(kwargs) + bstack11l111_opy_ (u"ࠢࠣᔎ"))
        bstack1lll111l1l1_opy_, bstack1lll1l11l1l_opy_ = bstack1lll11l11l1_opy_[0]
        driver = bstack1lll111l1l1_opy_()
        if not driver:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᔏ") + str(kwargs) + bstack11l111_opy_ (u"ࠤࠥᔐ"))
            return
        bstack11lllllll11_opy_ = {
            TestFramework.bstack1ll11l111ll_opy_: bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᔑ"),
            TestFramework.bstack1lll1l111l1_opy_: bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢᔒ"),
            TestFramework.bstack1ll11ll1lll_opy_: bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࠣࡶࡪࡸࡵ࡯ࠢࡱࡥࡲ࡫ࠢᔓ")
        }
        bstack11llllll1l1_opy_ = { key: f.get_state(instance, key) for key in bstack11lllllll11_opy_ }
        bstack11lllll1l1l_opy_ = [key for key, value in bstack11llllll1l1_opy_.items() if not value]
        if bstack11lllll1l1l_opy_:
            for key in bstack11lllll1l1l_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠤᔔ") + str(key) + bstack11l111_opy_ (u"ࠢࠣᔕ"))
            return
        platform_index = f.get_state(instance, bstack1lllllll1ll_opy_.bstack1111111l1l_opy_, 0)
        if self.bstack11lllll1lll_opy_.percy_capture_mode == bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᔖ"):
            bstack11ll1lllll_opy_ = bstack11llllll1l1_opy_.get(TestFramework.bstack1ll11ll1lll_opy_) + bstack11l111_opy_ (u"ࠤ࠰ࡸࡪࡹࡴࡤࡣࡶࡩࠧᔗ")
            bstack1ll11l1lll1_opy_ = bstack1lllll111l1_opy_.bstack1ll1l1l111l_opy_(EVENTS.bstack11llllllll1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11ll1lllll_opy_,
                bstack11ll1l111_opy_=bstack11llllll1l1_opy_[TestFramework.bstack1ll11l111ll_opy_],
                bstack1ll11l1ll1_opy_=bstack11llllll1l1_opy_[TestFramework.bstack1lll1l111l1_opy_],
                bstack11111lllll_opy_=platform_index
            )
            bstack1lllll111l1_opy_.end(EVENTS.bstack11llllllll1_opy_.value, bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᔘ"), bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᔙ"), True, None, None, None, None, test_name=bstack11ll1lllll_opy_)
    def bstack11ll11111l_opy_(self, driver, platform_index):
        if self.bstack11l1l1ll11_opy_.bstack1ll1ll1ll_opy_() is True or self.bstack11l1l1ll11_opy_.capturing() is True:
            return
        self.bstack11l1l1ll11_opy_.bstack111l11l1ll_opy_()
        while not self.bstack11l1l1ll11_opy_.bstack1ll1ll1ll_opy_():
            bstack11llllll11l_opy_ = self.bstack11l1l1ll11_opy_.bstack1111lllll_opy_()
            self.bstack11ll111ll_opy_(driver, bstack11llllll11l_opy_, platform_index)
        self.bstack11l1l1ll11_opy_.bstack1l1111l1l_opy_()
    def bstack11ll111ll_opy_(self, driver, bstack111ll1l1l1_opy_, platform_index, test=None):
        from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
        bstack1ll11l1lll1_opy_ = bstack1lllll111l1_opy_.bstack1ll1l1l111l_opy_(EVENTS.bstack111ll1111l_opy_.value)
        if test != None:
            bstack11ll1l111_opy_ = getattr(test, bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᔚ"), None)
            bstack1ll11l1ll1_opy_ = getattr(test, bstack11l111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᔛ"), None)
            PercySDK.screenshot(driver, bstack111ll1l1l1_opy_, bstack11ll1l111_opy_=bstack11ll1l111_opy_, bstack1ll11l1ll1_opy_=bstack1ll11l1ll1_opy_, bstack11111lllll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack111ll1l1l1_opy_)
        bstack1lllll111l1_opy_.end(EVENTS.bstack111ll1111l_opy_.value, bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᔜ"), bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᔝ"), True, None, None, None, None, test_name=bstack111ll1l1l1_opy_)
    def bstack11lllll1ll1_opy_(self):
        os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᔞ")] = str(self.bstack11lllll1lll_opy_.success)
        os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᔟ")] = str(self.bstack11lllll1lll_opy_.percy_capture_mode)
        self.percy.bstack11lllllll1l_opy_(self.bstack11lllll1lll_opy_.is_percy_auto_enabled)
        self.percy.bstack11llllll111_opy_(self.bstack11lllll1lll_opy_.percy_build_id)