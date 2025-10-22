# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llllllllll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1llll1l1l1l_opy_,
    bstack1lllllll111_opy_,
    bstack1llll11l1ll_opy_,
)
from bstack_utils.helper import  bstack1l111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1llll_opy_, bstack1lll1l1ll11_opy_, bstack1lll11lll1l_opy_, bstack1ll1l1111l1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11l1l1l11l_opy_ import bstack11l1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111lll1_opy_
from bstack_utils.percy import bstack111l1lll1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1ll11111l_opy_(bstack1llllllllll_opy_):
    def __init__(self, bstack11llll1llll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llll1llll_opy_ = bstack11llll1llll_opy_
        self.percy = bstack111l1lll1l_opy_()
        self.bstack1l1l1ll11_opy_ = bstack11l1l11l1l_opy_()
        self.bstack11lllll1l1l_opy_()
        bstack1lllllll11l_opy_.bstack1llll1ll1ll_opy_((bstack1llll1l1l1l_opy_.bstack1lllll111ll_opy_, bstack1lllllll111_opy_.PRE), self.bstack11lllll11ll_opy_)
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1llll111lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1l11l1_opy_(self, instance: bstack1llll11l1ll_opy_, driver: object):
        bstack1l11l1lll11_opy_ = TestFramework.bstack1l11l111ll1_opy_(instance.context)
        for t in bstack1l11l1lll11_opy_:
            bstack1lll111l11l_opy_ = TestFramework.get_state(t, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l11l_opy_) or instance == driver:
                return t
    def bstack11lllll11ll_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        bstack1llllll11l1_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllllll11l_opy_.bstack1l1ll1l1l1l_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllllll11l_opy_.bstack1llll1lll11_opy_, 0)
            bstack1ll11l11l11_opy_ = self.bstack1l11l1l11l1_opy_(instance, driver)
            bstack11llll1lll1_opy_ = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1ll111l11l1_opy_, None)
            if not bstack11llll1lll1_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡳࡧࡷࡹࡷࡴࡩ࡯ࡩࠣࡥࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡪࡵࠣࡲࡴࡺࠠࡺࡧࡷࠤࡸࡺࡡࡳࡶࡨࡨࠧᔶ"))
                return
            driver_command = f.bstack1l1ll1llll1_opy_(*args)
            for command in bstack1l1llllll1_opy_:
                if command == driver_command:
                    self.bstack1l11111lll_opy_(driver, platform_index)
            bstack111l1111l1_opy_ = self.percy.bstack11111llll_opy_()
            if driver_command in bstack1ll11l1111_opy_[bstack111l1111l1_opy_]:
                self.bstack1l1l1ll11_opy_.bstack11ll1l111l_opy_(bstack11llll1lll1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡧࡵࡶࡴࡸࠢᔷ"), e)
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
        bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
        if not bstack1lll111l11l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᔸ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠣࠤᔹ"))
            return
        if len(bstack1lll111l11l_opy_) > 1:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᔺ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠥࠦᔻ"))
        bstack1lll111llll_opy_, bstack1lll11ll1ll_opy_ = bstack1lll111l11l_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔼ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᔽ"))
            return
        bstack11llll1ll11_opy_ = {
            TestFramework.bstack1l1llllllll_opy_: bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᔾ"),
            TestFramework.bstack1llll111ll1_opy_: bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᔿ"),
            TestFramework.bstack1ll111l11l1_opy_: bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࠦࡲࡦࡴࡸࡲࠥࡴࡡ࡮ࡧࠥᕀ")
        }
        bstack11lllll111l_opy_ = { key: f.get_state(instance, key) for key in bstack11llll1ll11_opy_ }
        bstack11lllll11l1_opy_ = [key for key, value in bstack11lllll111l_opy_.items() if not value]
        if bstack11lllll11l1_opy_:
            for key in bstack11lllll11l1_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠧᕁ") + str(key) + bstack11l1l11_opy_ (u"ࠥࠦᕂ"))
            return
        platform_index = f.get_state(instance, bstack1lllllll11l_opy_.bstack1llll1lll11_opy_, 0)
        if self.bstack11llll1llll_opy_.percy_capture_mode == bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᕃ"):
            bstack11l1lll1l1_opy_ = bstack11lllll111l_opy_.get(TestFramework.bstack1ll111l11l1_opy_) + bstack11l1l11_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᕄ")
            bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack1ll1l11l111_opy_(EVENTS.bstack11lllll1111_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l1lll1l1_opy_,
                bstack111l1l1lll_opy_=bstack11lllll111l_opy_[TestFramework.bstack1l1llllllll_opy_],
                bstack1lllll111l_opy_=bstack11lllll111l_opy_[TestFramework.bstack1llll111ll1_opy_],
                bstack1111ll1lll_opy_=platform_index
            )
            bstack1llllll1ll1_opy_.end(EVENTS.bstack11lllll1111_opy_.value, bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᕅ"), bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᕆ"), True, None, None, None, None, test_name=bstack11l1lll1l1_opy_)
    def bstack1l11111lll_opy_(self, driver, platform_index):
        if self.bstack1l1l1ll11_opy_.bstack1ll111lll_opy_() is True or self.bstack1l1l1ll11_opy_.capturing() is True:
            return
        self.bstack1l1l1ll11_opy_.bstack1llll11ll1_opy_()
        while not self.bstack1l1l1ll11_opy_.bstack1ll111lll_opy_():
            bstack11llll1lll1_opy_ = self.bstack1l1l1ll11_opy_.bstack1lllll1ll1_opy_()
            self.bstack11l11ll1l_opy_(driver, bstack11llll1lll1_opy_, platform_index)
        self.bstack1l1l1ll11_opy_.bstack111ll1l1l_opy_()
    def bstack11l11ll1l_opy_(self, driver, bstack11ll1l1lll_opy_, platform_index, test=None):
        from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
        bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack1ll1l11l111_opy_(EVENTS.bstack111ll1llll_opy_.value)
        if test != None:
            bstack111l1l1lll_opy_ = getattr(test, bstack11l1l11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᕇ"), None)
            bstack1lllll111l_opy_ = getattr(test, bstack11l1l11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᕈ"), None)
            PercySDK.screenshot(driver, bstack11ll1l1lll_opy_, bstack111l1l1lll_opy_=bstack111l1l1lll_opy_, bstack1lllll111l_opy_=bstack1lllll111l_opy_, bstack1111ll1lll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11ll1l1lll_opy_)
        bstack1llllll1ll1_opy_.end(EVENTS.bstack111ll1llll_opy_.value, bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕉ"), bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᕊ"), True, None, None, None, None, test_name=bstack11ll1l1lll_opy_)
    def bstack11lllll1l1l_opy_(self):
        os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᕋ")] = str(self.bstack11llll1llll_opy_.success)
        os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᕌ")] = str(self.bstack11llll1llll_opy_.percy_capture_mode)
        self.percy.bstack11llll1ll1l_opy_(self.bstack11llll1llll_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll1l11_opy_(self.bstack11llll1llll_opy_.percy_build_id)