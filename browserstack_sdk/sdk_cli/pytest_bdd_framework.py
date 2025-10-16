# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1ll1lll1111_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l1l1111l_opy_ import bstack1ll1l111l1l_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l11lll_opy_,
    bstack1llll1l1111_opy_,
    bstack1llll1l11l1_opy_,
    bstack1ll1l1ll1ll_opy_,
    bstack1ll11l1l11l_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l1lll11_opy_
from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll111111l1_opy_ import bstack1ll11l11ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
bstack1ll111ll1l1_opy_ = bstack1ll1l1lll11_opy_()
bstack1ll11ll11ll_opy_ = bstack1ll1ll1_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥᇺ")
bstack1ll1111l1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢᇻ")
bstack1ll1l111l11_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦᇼ")
bstack1ll1l1l1l1l_opy_ = 1.0
_1ll1l111lll_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l1l111l_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᇽ")
    bstack1ll11l1llll_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧᇾ")
    bstack1ll1111111l_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᇿ")
    bstack1ll111ll111_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦሀ")
    bstack1ll1l11ll11_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨሁ")
    bstack1ll1l1lll1l_opy_: bool
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_  = None
    bstack1ll1ll11l11_opy_ = [
        bstack1lll1l11lll_opy_.BEFORE_ALL,
        bstack1lll1l11lll_opy_.AFTER_ALL,
        bstack1lll1l11lll_opy_.BEFORE_EACH,
        bstack1lll1l11lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111l1l11_opy_: Dict[str, str],
        bstack1ll11111l1l_opy_: List[str]=[bstack1ll1ll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣሂ")],
        bstack1lll1l11111_opy_: bstack1lll11lllll_opy_ = None,
        bstack1lllll1lll1_opy_=None
    ):
        super().__init__(bstack1ll11111l1l_opy_, bstack1ll111l1l11_opy_, bstack1lll1l11111_opy_)
        self.bstack1ll1l1lll1l_opy_ = any(bstack1ll1ll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤሃ") in item.lower() for item in bstack1ll11111l1l_opy_)
        self.bstack1lllll1lll1_opy_ = bstack1lllll1lll1_opy_
    def track_event(
        self,
        context: bstack1ll1l1ll1ll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l11lll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1ll11l11_opy_:
            bstack1ll1l111l1l_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l11lll_opy_.NONE:
            self.logger.warning(bstack1ll1ll1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢሄ") + str(test_hook_state) + bstack1ll1ll1_opy_ (u"ࠢࠣህ"))
            return
        if not self.bstack1ll1l1lll1l_opy_:
            self.logger.warning(bstack1ll1ll1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤሆ") + str(str(self.bstack1ll11111l1l_opy_)) + bstack1ll1ll1_opy_ (u"ࠤࠥሇ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1ll1ll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧለ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠦࠧሉ"))
            return
        instance = self.__1l1lllllll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦሊ") + str(args) + bstack1ll1ll1_opy_ (u"ࠨࠢላ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1ll11l11_opy_ and test_hook_state == bstack1llll1l11l1_opy_.PRE:
                bstack1ll111l11ll_opy_ = bstack1lllll1l11l_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack11111lll11_opy_.value)
                name = str(EVENTS.bstack11111lll11_opy_.name)+bstack1ll1ll1_opy_ (u"ࠢ࠻ࠤሌ")+str(test_framework_state.name)
                TestFramework.bstack1ll11lll1ll_opy_(instance, name, bstack1ll111l11ll_opy_)
        except Exception as e:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧል").format(e))
        try:
            if test_framework_state == bstack1lll1l11lll_opy_.TEST:
                if not TestFramework.bstack1lllll1ll11_opy_(instance, TestFramework.bstack1ll11ll111l_opy_) and test_hook_state == bstack1llll1l11l1_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1l11l1ll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሎ") + str(test_hook_state) + bstack1ll1ll1_opy_ (u"ࠥࠦሏ"))
                if test_hook_state == bstack1llll1l11l1_opy_.PRE and not TestFramework.bstack1lllll1ll11_opy_(instance, TestFramework.bstack1ll1l1l1111_opy_):
                    TestFramework.bstack1lllll1l1ll_opy_(instance, TestFramework.bstack1ll1l1l1111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1111l11l_opy_(instance, args)
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሐ") + str(test_hook_state) + bstack1ll1ll1_opy_ (u"ࠧࠨሑ"))
                elif test_hook_state == bstack1llll1l11l1_opy_.POST and not TestFramework.bstack1lllll1ll11_opy_(instance, TestFramework.bstack1ll11ll1lll_opy_):
                    TestFramework.bstack1lllll1l1ll_opy_(instance, TestFramework.bstack1ll11ll1lll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሒ") + str(test_hook_state) + bstack1ll1ll1_opy_ (u"ࠢࠣሓ"))
            elif test_framework_state == bstack1lll1l11lll_opy_.STEP:
                if test_hook_state == bstack1llll1l11l1_opy_.PRE:
                    PytestBDDFramework.__1ll11l111ll_opy_(instance, args)
                elif test_hook_state == bstack1llll1l11l1_opy_.POST:
                    PytestBDDFramework.__1ll111111ll_opy_(instance, args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG and test_hook_state == bstack1llll1l11l1_opy_.POST:
                PytestBDDFramework.__1ll1111llll_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG_REPORT and test_hook_state == bstack1llll1l11l1_opy_.POST:
                self.__1ll1ll111ll_opy_(instance, *args)
                self.__1ll1l11l1l1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1ll11l11_opy_:
                self.__1l1llllll11_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤሔ") + str(instance.ref()) + bstack1ll1ll1_opy_ (u"ࠤࠥሕ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l1111ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1ll11l11_opy_ and test_hook_state == bstack1llll1l11l1_opy_.POST:
                name = str(EVENTS.bstack11111lll11_opy_.name)+bstack1ll1ll1_opy_ (u"ࠥ࠾ࠧሖ")+str(test_framework_state.name)
                bstack1ll111l11ll_opy_ = TestFramework.bstack1ll11l1111l_opy_(instance, name)
                bstack1lllll1l11l_opy_.end(EVENTS.bstack11111lll11_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦሗ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥመ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨሙ").format(e))
    def bstack1ll1l1l11ll_opy_(self):
        return self.bstack1ll1l1lll1l_opy_
    def __1ll111lllll_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1ll1ll1_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦሚ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l11l1_opy_(rep, [bstack1ll1ll1_opy_ (u"ࠣࡹ࡫ࡩࡳࠨማ"), bstack1ll1ll1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥሜ"), bstack1ll1ll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥም"), bstack1ll1ll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦሞ"), bstack1ll1ll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨሟ"), bstack1ll1ll1_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧሠ")])
        return None
    def __1ll1ll111ll_opy_(self, instance: bstack1llll1l1111_opy_, *args):
        result = self.__1ll111lllll_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l11l1_opy_ = None
        if result.get(bstack1ll1ll1_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣሡ"), None) == bstack1ll1ll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣሢ") and len(args) > 1 and getattr(args[1], bstack1ll1ll1_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥሣ"), None) is not None:
            failure = [{bstack1ll1ll1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ሤ"): [args[1].excinfo.exconly(), result.get(bstack1ll1ll1_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥሥ"), None)]}]
            bstack11111l11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨሦ") if bstack1ll1ll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤሧ") in getattr(args[1].excinfo, bstack1ll1ll1_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤረ"), bstack1ll1ll1_opy_ (u"ࠣࠤሩ")) else bstack1ll1ll1_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥሪ")
        bstack1ll1l1lllll_opy_ = result.get(bstack1ll1ll1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦራ"), TestFramework.bstack1ll11ll1111_opy_)
        if bstack1ll1l1lllll_opy_ != TestFramework.bstack1ll11ll1111_opy_:
            TestFramework.bstack1lllll1l1ll_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1ll111l1_opy_(instance, {
            TestFramework.bstack1lll1ll1111_opy_: failure,
            TestFramework.bstack1ll11llllll_opy_: bstack11111l11l1_opy_,
            TestFramework.bstack1lll1lll1ll_opy_: bstack1ll1l1lllll_opy_,
        })
    def __1l1lllllll1_opy_(
        self,
        context: bstack1ll1l1ll1ll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l11lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l11l111_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1lllll1l1_opy_ bstack1l1lllll111_opy_ this to be bstack1ll1ll1_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሬ")
            if test_framework_state == bstack1lll1l11lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11l11111_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1ll1ll1_opy_ (u"ࠧࡴ࡯ࡥࡧࠥር"), None), bstack1ll1ll1_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨሮ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1ll1ll1_opy_ (u"ࠢ࡯ࡱࡧࡩࠧሯ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1ll1ll1_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣሰ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111ll11l_opy_(target) if target else None
        return instance
    def __1l1llllll11_opy_(
        self,
        instance: bstack1llll1l1111_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1llllllll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l1llll_opy_, {})
        if not key in bstack1l1llllllll_opy_:
            bstack1l1llllllll_opy_[key] = []
        bstack1ll11l1l111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1111111l_opy_, {})
        if not key in bstack1ll11l1l111_opy_:
            bstack1ll11l1l111_opy_[key] = []
        bstack1ll1l1ll1l1_opy_ = {
            PytestBDDFramework.bstack1ll11l1llll_opy_: bstack1l1llllllll_opy_,
            PytestBDDFramework.bstack1ll1111111l_opy_: bstack1ll11l1l111_opy_,
        }
        if test_hook_state == bstack1llll1l11l1_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1ll1ll1_opy_ (u"ࠤ࡮ࡩࡾࠨሱ"): key,
                TestFramework.bstack1ll1l1ll11l_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l11llll_opy_: TestFramework.bstack1ll11lll111_opy_,
                TestFramework.bstack1ll11111111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1l111111_opy_: [],
                TestFramework.bstack1ll11111ll1_opy_: hook_name,
                TestFramework.bstack1ll1l11111l_opy_: bstack1ll11l11ll1_opy_.bstack1ll1l1l1lll_opy_()
            }
            bstack1l1llllllll_opy_[key].append(hook)
            bstack1ll1l1ll1l1_opy_[PytestBDDFramework.bstack1ll111ll111_opy_] = key
        elif test_hook_state == bstack1llll1l11l1_opy_.POST:
            bstack1l1llll1lll_opy_ = bstack1l1llllllll_opy_.get(key, [])
            hook = bstack1l1llll1lll_opy_.pop() if bstack1l1llll1lll_opy_ else None
            if hook:
                result = self.__1ll111lllll_opy_(*args)
                if result:
                    bstack1ll111lll1l_opy_ = result.get(bstack1ll1ll1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦሲ"), TestFramework.bstack1ll11lll111_opy_)
                    if bstack1ll111lll1l_opy_ != TestFramework.bstack1ll11lll111_opy_:
                        hook[TestFramework.bstack1ll1l11llll_opy_] = bstack1ll111lll1l_opy_
                hook[TestFramework.bstack1ll111lll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l11111l_opy_] = bstack1ll11l11ll1_opy_.bstack1ll1l1l1lll_opy_()
                self.bstack1ll11111l11_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l1l1l11_opy_, [])
                self.bstack1ll1ll1111l_opy_(instance, logs)
                bstack1ll11l1l111_opy_[key].append(hook)
                bstack1ll1l1ll1l1_opy_[PytestBDDFramework.bstack1ll1l11ll11_opy_] = key
        TestFramework.bstack1ll1ll111l1_opy_(instance, bstack1ll1l1ll1l1_opy_)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥሳ") + str(bstack1ll11l1l111_opy_) + bstack1ll1ll1_opy_ (u"ࠧࠨሴ"))
    def __1ll1l11l111_opy_(
        self,
        context: bstack1ll1l1ll1ll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l11l1_opy_(args[0], [bstack1ll1ll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧስ"), bstack1ll1ll1_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣሶ"), bstack1ll1ll1_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣሷ"), bstack1ll1ll1_opy_ (u"ࠤ࡬ࡨࡸࠨሸ"), bstack1ll1ll1_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧሹ"), bstack1ll1ll1_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦሺ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1ll1ll1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦሻ")) else fixturedef.get(bstack1ll1ll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧሼ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1ll1ll1_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧሽ")) else None
        node = request.node if hasattr(request, bstack1ll1ll1_opy_ (u"ࠣࡰࡲࡨࡪࠨሾ")) else None
        target = request.node.nodeid if hasattr(node, bstack1ll1ll1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሿ")) else None
        baseid = fixturedef.get(bstack1ll1ll1_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥቀ"), None) or bstack1ll1ll1_opy_ (u"ࠦࠧቁ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1ll1ll1_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥቂ")):
            target = PytestBDDFramework.__1ll1l1ll111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1ll1ll1_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣቃ")) else None
            if target and not TestFramework.bstack1ll111ll11l_opy_(target):
                self.__1ll11l11111_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤቄ") + str(test_hook_state) + bstack1ll1ll1_opy_ (u"ࠣࠤቅ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1ll1ll1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢቆ") + str(target) + bstack1ll1ll1_opy_ (u"ࠥࠦቇ"))
            return None
        instance = TestFramework.bstack1ll111ll11l_opy_(target)
        if not instance:
            self.logger.warning(bstack1ll1ll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨቈ") + str(target) + bstack1ll1ll1_opy_ (u"ࠧࠨ቉"))
            return None
        bstack1ll11lllll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l1l111l_opy_, {})
        if os.getenv(bstack1ll1ll1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢቊ"), bstack1ll1ll1_opy_ (u"ࠢ࠲ࠤቋ")) == bstack1ll1ll1_opy_ (u"ࠣ࠳ࠥቌ"):
            bstack1ll111l1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠤ࠽ࠦቍ").join((scope, fixturename))
            bstack1ll1111l1ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l11l11l_opy_ = {
                bstack1ll1ll1_opy_ (u"ࠥ࡯ࡪࡿࠢ቎"): bstack1ll111l1lll_opy_,
                bstack1ll1ll1_opy_ (u"ࠦࡹࡧࡧࡴࠤ቏"): PytestBDDFramework.__1l1lllll1ll_opy_(request.node, scenario),
                bstack1ll1ll1_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨቐ"): fixturedef,
                bstack1ll1ll1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቑ"): scope,
                bstack1ll1ll1_opy_ (u"ࠢࡵࡻࡳࡩࠧቒ"): None,
            }
            try:
                if test_hook_state == bstack1llll1l11l1_opy_.POST and callable(getattr(args[-1], bstack1ll1ll1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧቓ"), None)):
                    bstack1ll1l11l11l_opy_[bstack1ll1ll1_opy_ (u"ࠤࡷࡽࡵ࡫ࠢቔ")] = TestFramework.bstack1ll1l11lll1_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1llll1l11l1_opy_.PRE:
                bstack1ll1l11l11l_opy_[bstack1ll1ll1_opy_ (u"ࠥࡹࡺ࡯ࡤࠣቕ")] = uuid4().__str__()
                bstack1ll1l11l11l_opy_[PytestBDDFramework.bstack1ll11111111_opy_] = bstack1ll1111l1ll_opy_
            elif test_hook_state == bstack1llll1l11l1_opy_.POST:
                bstack1ll1l11l11l_opy_[PytestBDDFramework.bstack1ll111lll11_opy_] = bstack1ll1111l1ll_opy_
            if bstack1ll111l1lll_opy_ in bstack1ll11lllll1_opy_:
                bstack1ll11lllll1_opy_[bstack1ll111l1lll_opy_].update(bstack1ll1l11l11l_opy_)
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧቖ") + str(bstack1ll11lllll1_opy_[bstack1ll111l1lll_opy_]) + bstack1ll1ll1_opy_ (u"ࠧࠨ቗"))
            else:
                bstack1ll11lllll1_opy_[bstack1ll111l1lll_opy_] = bstack1ll1l11l11l_opy_
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤቘ") + str(len(bstack1ll11lllll1_opy_)) + bstack1ll1ll1_opy_ (u"ࠢࠣ቙"))
        TestFramework.bstack1lllll1l1ll_opy_(instance, PytestBDDFramework.bstack1ll1l1l111l_opy_, bstack1ll11lllll1_opy_)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣቚ") + str(instance.ref()) + bstack1ll1ll1_opy_ (u"ࠤࠥቛ"))
        return instance
    def __1ll11l11111_opy_(
        self,
        context: bstack1ll1l1ll1ll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll1111_opy_.create_context(target)
        ob = bstack1llll1l1111_opy_(ctx, self.bstack1ll11111l1l_opy_, self.bstack1ll111l1l11_opy_, test_framework_state)
        TestFramework.bstack1ll1ll111l1_opy_(ob, {
            TestFramework.bstack1llll11111l_opy_: context.test_framework_name,
            TestFramework.bstack1llll111111_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l1111l1_opy_: [],
            PytestBDDFramework.bstack1ll1l1l111l_opy_: {},
            PytestBDDFramework.bstack1ll1111111l_opy_: {},
            PytestBDDFramework.bstack1ll11l1llll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll1l1ll_opy_(ob, TestFramework.bstack1ll11lll1l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll1l1ll_opy_(ob, TestFramework.bstack1111111ll1_opy_, context.platform_index)
        TestFramework.bstack1lll1l1ll1l_opy_[ctx.id] = ob
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥቜ") + str(TestFramework.bstack1lll1l1ll1l_opy_.keys()) + bstack1ll1ll1_opy_ (u"ࠦࠧቝ"))
        return ob
    @staticmethod
    def __1ll1111l11l_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࠨ቞"): id(step),
                bstack1ll1ll1_opy_ (u"࠭ࡴࡦࡺࡷࠫ቟"): step.name,
                bstack1ll1ll1_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨበ"): step.keyword,
            })
        meta = {
            bstack1ll1ll1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩቡ"): {
                bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧቢ"): feature.name,
                bstack1ll1ll1_opy_ (u"ࠪࡴࡦࡺࡨࠨባ"): feature.filename,
                bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩቤ"): feature.description
            },
            bstack1ll1ll1_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧብ"): {
                bstack1ll1ll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫቦ"): scenario.name
            },
            bstack1ll1ll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ቧ"): steps,
            bstack1ll1ll1_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪቨ"): PytestBDDFramework.__1ll11111lll_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll1ll11111_opy_: meta
            }
        )
    def bstack1ll11111l11_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1ll1ll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡴ࡫ࡰ࡭ࡱࡧࡲࠡࡶࡲࠤࡹ࡮ࡥࠡࡌࡤࡺࡦࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡃࡩࡧࡦ࡯ࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡬ࡲࡸ࡯ࡤࡦࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠳࡚ࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡵࡩࡵࡲࡡࡤࡧࡶࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦࠥ࡯࡮ࠡ࡫ࡷࡷࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡌࡪࠥࡧࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡯ࡤࡸࡨ࡮ࡥࡴࠢࡤࠤࡲࡵࡤࡪࡨ࡬ࡩࡩࠦࡨࡰࡱ࡮࠱ࡱ࡫ࡶࡦ࡮ࠣࡪ࡮ࡲࡥ࠭ࠢ࡬ࡸࠥࡩࡲࡦࡣࡷࡩࡸࠦࡡࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࠣࡻ࡮ࡺࡨࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡙ࠥࡩ࡮࡫࡯ࡥࡷࡲࡹ࠭ࠢ࡬ࡸࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡴࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡥࡽࠥࡸࡥࡱ࡮ࡤࡧ࡮ࡴࡧࠡࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡖ࡫ࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡤࡶࡪࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥ࡮࡯ࡰ࡭ࠪࡷࠥࠨ࡬ࡰࡩࡶࠦࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࠺ࠡࡖ࡫ࡩࠥ࡫ࡶࡦࡰࡷࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷࠥࡧ࡮ࡥࠢ࡫ࡳࡴࡱࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡘࡪࡹࡴࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣቩ")
        global _1ll1l111lll_opy_
        platform_index = os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪቪ")]
        bstack1ll11l11lll_opy_ = os.path.join(bstack1ll111ll1l1_opy_, (bstack1ll11ll11ll_opy_ + str(platform_index)), bstack1ll1111l1l1_opy_)
        if not os.path.exists(bstack1ll11l11lll_opy_) or not os.path.isdir(bstack1ll11l11lll_opy_):
            return
        logs = hook.get(bstack1ll1ll1_opy_ (u"ࠦࡱࡵࡧࡴࠤቫ"), [])
        with os.scandir(bstack1ll11l11lll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l111lll_opy_:
                    self.logger.info(bstack1ll1ll1_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥቬ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1ll1ll1_opy_ (u"ࠨࠢቭ")
                    log_entry = bstack1ll11l1l11l_opy_(
                        kind=bstack1ll1ll1_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤቮ"),
                        message=bstack1ll1ll1_opy_ (u"ࠣࠤቯ"),
                        level=bstack1ll1ll1_opy_ (u"ࠤࠥተ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l1ll11_opy_=entry.stat().st_size,
                        bstack1ll1111lll1_opy_=bstack1ll1ll1_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥቱ"),
                        bstack1l1111l_opy_=os.path.abspath(entry.path),
                        bstack1ll11l1lll1_opy_=hook.get(TestFramework.bstack1ll1l1ll11l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l111lll_opy_.add(abs_path)
        platform_index = os.environ[bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫቲ")]
        bstack1l1llllll1l_opy_ = os.path.join(bstack1ll111ll1l1_opy_, (bstack1ll11ll11ll_opy_ + str(platform_index)), bstack1ll1111l1l1_opy_, bstack1ll1l111l11_opy_)
        if not os.path.exists(bstack1l1llllll1l_opy_) or not os.path.isdir(bstack1l1llllll1l_opy_):
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠧࡔ࡯ࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡨࡲࡹࡳࡪࠠࡢࡶ࠽ࠤࢀࢃࠢታ").format(bstack1l1llllll1l_opy_))
        else:
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡧࡴࡲࡱࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠻ࠢࡾࢁࠧቴ").format(bstack1l1llllll1l_opy_))
            with os.scandir(bstack1l1llllll1l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l111lll_opy_:
                        self.logger.info(bstack1ll1ll1_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧት").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1ll1ll1_opy_ (u"ࠣࠤቶ")
                        log_entry = bstack1ll11l1l11l_opy_(
                            kind=bstack1ll1ll1_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦቷ"),
                            message=bstack1ll1ll1_opy_ (u"ࠥࠦቸ"),
                            level=bstack1ll1ll1_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣቹ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l1ll11_opy_=entry.stat().st_size,
                            bstack1ll1111lll1_opy_=bstack1ll1ll1_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧቺ"),
                            bstack1l1111l_opy_=os.path.abspath(entry.path),
                            bstack1ll11llll11_opy_=hook.get(TestFramework.bstack1ll1l1ll11l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l111lll_opy_.add(abs_path)
        hook[bstack1ll1ll1_opy_ (u"ࠨ࡬ࡰࡩࡶࠦቻ")] = logs
    def bstack1ll1ll1111l_opy_(
        self,
        bstack1ll1ll11l1l_opy_: bstack1llll1l1111_opy_,
        entries: List[bstack1ll11l1l11l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1ll1ll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦቼ"))
        req.platform_index = TestFramework.get_state(bstack1ll1ll11l1l_opy_, TestFramework.bstack1111111ll1_opy_)
        req.execution_context.hash = str(bstack1ll1ll11l1l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1ll11l1l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1ll11l1l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1ll11l1l_opy_, TestFramework.bstack1llll11111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1ll11l1l_opy_, TestFramework.bstack1llll111111_opy_)
            log_entry.uuid = entry.bstack1ll11l1lll1_opy_ if entry.bstack1ll11l1lll1_opy_ else TestFramework.get_state(bstack1ll1ll11l1l_opy_, TestFramework.bstack1lll1l1l1l1_opy_)
            log_entry.test_framework_state = bstack1ll1ll11l1l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1ll1ll1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢች"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1ll1ll1_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦቾ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1ll11_opy_
                log_entry.file_path = entry.bstack1l1111l_opy_
        def bstack1ll11ll1l11_opy_():
            bstack111lllll1_opy_ = datetime.now()
            try:
                self.bstack1lllll1lll1_opy_.LogCreatedEvent(req)
                bstack1ll1ll11l1l_opy_.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢቿ"), datetime.now() - bstack111lllll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll1ll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡼࡿࠥኀ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll11ll1l11_opy_)
    def __1ll1l11l1l1_opy_(self, instance) -> None:
        bstack1ll1ll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡏࡳࡦࡪࡳࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡸࡥࡢࡶࡨࡷࠥࡧࠠࡥ࡫ࡦࡸࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡡ࡯ࡦࠣࡹࡵࡪࡡࡵࡧࡶࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡷࡹࡧࡴࡦࠢࡸࡷ࡮ࡴࡧࠡࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኁ")
        bstack1ll1l1ll1l1_opy_ = {bstack1ll1ll1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣኂ"): bstack1ll11l11ll1_opy_.bstack1ll1l1l1lll_opy_()}
        TestFramework.bstack1ll1ll111l1_opy_(instance, bstack1ll1l1ll1l1_opy_)
    @staticmethod
    def __1ll11l111ll_opy_(instance, args):
        request, bstack1ll1111l111_opy_ = args
        bstack1ll1l11ll1l_opy_ = id(bstack1ll1111l111_opy_)
        bstack1ll11l1l1l1_opy_ = instance.data[TestFramework.bstack1ll1ll11111_opy_]
        step = next(filter(lambda st: st[bstack1ll1ll1_opy_ (u"ࠧࡪࡦࠪኃ")] == bstack1ll1l11ll1l_opy_, bstack1ll11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኄ")]), None)
        step.update({
            bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ኅ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኆ")]) if st[bstack1ll1ll1_opy_ (u"ࠫ࡮ࡪࠧኇ")] == step[bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࠨኈ")]), None)
        if index is not None:
            bstack1ll11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ኉")][index] = step
        instance.data[TestFramework.bstack1ll1ll11111_opy_] = bstack1ll11l1l1l1_opy_
    @staticmethod
    def __1ll111111ll_opy_(instance, args):
        bstack1ll1ll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡮ࡥ࡯ࠢ࡯ࡩࡳࠦࡡࡳࡩࡶࠤ࡮ࡹࠠ࠳࠮ࠣ࡭ࡹࠦࡳࡪࡩࡱ࡭࡫࡯ࡥࡴࠢࡷ࡬ࡪࡸࡥࠡ࡫ࡶࠤࡳࡵࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࡸࠦࡡࡳࡧࠣ࠱ࠥࡡࡲࡦࡳࡸࡩࡸࡺࠬࠡࡵࡷࡩࡵࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠳ࠡࡶ࡫ࡩࡳࠦࡴࡩࡧࠣࡰࡦࡹࡴࠡࡸࡤࡰࡺ࡫ࠠࡪࡵࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኊ")
        bstack1ll111llll1_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1111l111_opy_ = args[1]
        bstack1ll1l11ll1l_opy_ = id(bstack1ll1111l111_opy_)
        bstack1ll11l1l1l1_opy_ = instance.data[TestFramework.bstack1ll1ll11111_opy_]
        step = None
        if bstack1ll1l11ll1l_opy_ is not None and bstack1ll11l1l1l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኋ")):
            step = next(filter(lambda st: st[bstack1ll1ll1_opy_ (u"ࠩ࡬ࡨࠬኌ")] == bstack1ll1l11ll1l_opy_, bstack1ll11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኍ")]), None)
            step.update({
                bstack1ll1ll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ኎"): bstack1ll111llll1_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1ll1ll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ኏"): bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ነ"),
                bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨኑ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1ll1ll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨኒ"): bstack1ll1ll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩና"),
                })
        index = next((i for i, st in enumerate(bstack1ll11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኔ")]) if st[bstack1ll1ll1_opy_ (u"ࠫ࡮ࡪࠧን")] == step[bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࠨኖ")]), None)
        if index is not None:
            bstack1ll11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኗ")][index] = step
        instance.data[TestFramework.bstack1ll1ll11111_opy_] = bstack1ll11l1l1l1_opy_
    @staticmethod
    def __1ll11111lll_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1ll1ll1_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩኘ")):
                examples = list(node.callspec.params[bstack1ll1ll1_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧኙ")].values())
            return examples
        except:
            return []
    def bstack1l1lllll11l_opy_(self, instance: bstack1llll1l1111_opy_, bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_]):
        bstack1ll111l11l1_opy_ = (
            PytestBDDFramework.bstack1ll111ll111_opy_
            if bstack1llll1l1lll_opy_[1] == bstack1llll1l11l1_opy_.PRE
            else PytestBDDFramework.bstack1ll1l11ll11_opy_
        )
        hook = PytestBDDFramework.bstack1ll11ll1l1l_opy_(instance, bstack1ll111l11l1_opy_)
        entries = hook.get(TestFramework.bstack1ll1l111111_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l1111l1_opy_, []))
        return entries
    def bstack1ll11ll1ll1_opy_(self, instance: bstack1llll1l1111_opy_, bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_]):
        bstack1ll111l11l1_opy_ = (
            PytestBDDFramework.bstack1ll111ll111_opy_
            if bstack1llll1l1lll_opy_[1] == bstack1llll1l11l1_opy_.PRE
            else PytestBDDFramework.bstack1ll1l11ll11_opy_
        )
        PytestBDDFramework.bstack1ll1l1l1ll1_opy_(instance, bstack1ll111l11l1_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l1111l1_opy_, []).clear()
    @staticmethod
    def bstack1ll11ll1l1l_opy_(instance: bstack1llll1l1111_opy_, bstack1ll111l11l1_opy_: str):
        bstack1ll1l111ll1_opy_ = (
            PytestBDDFramework.bstack1ll1111111l_opy_
            if bstack1ll111l11l1_opy_ == PytestBDDFramework.bstack1ll1l11ll11_opy_
            else PytestBDDFramework.bstack1ll11l1llll_opy_
        )
        bstack1ll111l111l_opy_ = TestFramework.get_state(instance, bstack1ll111l11l1_opy_, None)
        bstack1ll1l1llll1_opy_ = TestFramework.get_state(instance, bstack1ll1l111ll1_opy_, None) if bstack1ll111l111l_opy_ else None
        return (
            bstack1ll1l1llll1_opy_[bstack1ll111l111l_opy_][-1]
            if isinstance(bstack1ll1l1llll1_opy_, dict) and len(bstack1ll1l1llll1_opy_.get(bstack1ll111l111l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l1l1ll1_opy_(instance: bstack1llll1l1111_opy_, bstack1ll111l11l1_opy_: str):
        hook = PytestBDDFramework.bstack1ll11ll1l1l_opy_(instance, bstack1ll111l11l1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1l111111_opy_, []).clear()
    @staticmethod
    def __1ll1111llll_opy_(instance: bstack1llll1l1111_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1ll1ll1_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡥࡲࡶࡩࡹࠢኚ"), None)):
            return
        if os.getenv(bstack1ll1ll1_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡏࡓࡌ࡙ࠢኛ"), bstack1ll1ll1_opy_ (u"ࠦ࠶ࠨኜ")) != bstack1ll1ll1_opy_ (u"ࠧ࠷ࠢኝ"):
            PytestBDDFramework.logger.warning(bstack1ll1ll1_opy_ (u"ࠨࡩࡨࡰࡲࡶ࡮ࡴࡧࠡࡥࡤࡴࡱࡵࡧࠣኞ"))
            return
        bstack1ll1111ll11_opy_ = {
            bstack1ll1ll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨኟ"): (PytestBDDFramework.bstack1ll111ll111_opy_, PytestBDDFramework.bstack1ll11l1llll_opy_),
            bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥአ"): (PytestBDDFramework.bstack1ll1l11ll11_opy_, PytestBDDFramework.bstack1ll1111111l_opy_),
        }
        for when in (bstack1ll1ll1_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣኡ"), bstack1ll1ll1_opy_ (u"ࠥࡧࡦࡲ࡬ࠣኢ"), bstack1ll1ll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨኣ")):
            bstack1ll111l1ll1_opy_ = args[1].get_records(when)
            if not bstack1ll111l1ll1_opy_:
                continue
            records = [
                bstack1ll11l1l11l_opy_(
                    kind=TestFramework.bstack1ll11l1ll1l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1ll1ll1_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠣኤ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1ll1ll1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪࠢእ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll111l1ll1_opy_
                if isinstance(getattr(r, bstack1ll1ll1_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣኦ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11ll11l1_opy_, bstack1ll1l111ll1_opy_ = bstack1ll1111ll11_opy_.get(when, (None, None))
            bstack1ll11l111l1_opy_ = TestFramework.get_state(instance, bstack1ll11ll11l1_opy_, None) if bstack1ll11ll11l1_opy_ else None
            bstack1ll1l1llll1_opy_ = TestFramework.get_state(instance, bstack1ll1l111ll1_opy_, None) if bstack1ll11l111l1_opy_ else None
            if isinstance(bstack1ll1l1llll1_opy_, dict) and len(bstack1ll1l1llll1_opy_.get(bstack1ll11l111l1_opy_, [])) > 0:
                hook = bstack1ll1l1llll1_opy_[bstack1ll11l111l1_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1l111111_opy_ in hook:
                    hook[TestFramework.bstack1ll1l111111_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l1111l1_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l11l1ll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll111l1111_opy_(request.node, scenario)
        bstack1ll111l1l1l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll111l1l1l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1l1l1l1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11ll111l_opy_: test_id,
            TestFramework.bstack1ll11l11l11_opy_: test_name,
            TestFramework.bstack1ll11lll11l_opy_: test_id,
            TestFramework.bstack1ll11llll1l_opy_: bstack1ll111l1l1l_opy_,
            TestFramework.bstack1ll1111ll1l_opy_: PytestBDDFramework.__1l1lllll1ll_opy_(feature, scenario),
            TestFramework.bstack1ll11l1l1ll_opy_: code,
            TestFramework.bstack1lll1lll1ll_opy_: TestFramework.bstack1ll11ll1111_opy_,
            TestFramework.bstack1lll11l1lll_opy_: test_name
        }
    @staticmethod
    def __1ll111l1111_opy_(node, scenario):
        if hasattr(node, bstack1ll1ll1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪኧ")):
            parts = node.nodeid.rsplit(bstack1ll1ll1_opy_ (u"ࠤ࡞ࠦከ"))
            params = parts[-1]
            return bstack1ll1ll1_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥኩ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1l1lllll1ll_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1ll1ll1_opy_ (u"ࠫࡹࡧࡧࡴࠩኪ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1ll1ll1_opy_ (u"ࠬࡺࡡࡨࡵࠪካ")) else [])
    @staticmethod
    def __1ll1l1ll111_opy_(location):
        return bstack1ll1ll1_opy_ (u"ࠨ࠺࠻ࠤኬ").join(filter(lambda x: isinstance(x, str), location))