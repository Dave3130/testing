# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1ll1ll11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11111l1_opy_ import bstack1l1lll1llll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll111l1l_opy_,
    bstack1lll1l1llll_opy_,
    bstack1lll1lll111_opy_,
    bstack1ll11l11l11_opy_,
    bstack1ll1l1l1ll1_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l1ll11l_opy_
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1lll11l1l1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1lll1lll1_opy_ import bstack1ll1111ll11_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11l1l_opy_
bstack1ll11ll1111_opy_ = bstack1ll1l1ll11l_opy_()
bstack1ll1l11llll_opy_ = 1.0
bstack1ll11lll11l_opy_ = bstack1lllll1l_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧᖊ")
bstack11llll11l11_opy_ = bstack1lllll1l_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᖋ")
bstack11llll11111_opy_ = bstack1lllll1l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᖌ")
bstack11llll111l1_opy_ = bstack1lllll1l_opy_ (u"ࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦᖍ")
bstack11llll1111l_opy_ = bstack1lllll1l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣᖎ")
_1ll111l11l1_opy_ = set()
class bstack1l1l1ll111l_opy_(TestFramework):
    bstack1ll1l111ll1_opy_ = bstack1lllll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᖏ")
    bstack1ll11l11ll1_opy_ = bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࠤᖐ")
    bstack1l1llll1ll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᖑ")
    bstack1l1llll111l_opy_ = bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣᖒ")
    bstack1ll111l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥᖓ")
    bstack1ll111111l1_opy_: bool
    bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_  = None
    bstack1lllllll111_opy_ = None
    bstack1ll11l11l1l_opy_ = [
        bstack1llll111l1l_opy_.BEFORE_ALL,
        bstack1llll111l1l_opy_.AFTER_ALL,
        bstack1llll111l1l_opy_.BEFORE_EACH,
        bstack1llll111l1l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111llll1_opy_: Dict[str, str],
        bstack1ll1l1l11ll_opy_: List[str]=[bstack1lllll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᖔ")],
        bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_=None,
        bstack1lllllll111_opy_=None
    ):
        super().__init__(bstack1ll1l1l11ll_opy_, bstack1ll111llll1_opy_, bstack1lll11l1l11_opy_)
        self.bstack1ll111111l1_opy_ = any(bstack1lllll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᖕ") in item.lower() for item in bstack1ll1l1l11ll_opy_)
        self.bstack1lllllll111_opy_ = bstack1lllllll111_opy_
    def track_event(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll111l1l_opy_.TEST or test_framework_state in bstack1l1l1ll111l_opy_.bstack1ll11l11l1l_opy_:
            bstack1l1lll1llll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll111l1l_opy_.NONE:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧࡧࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࠦᖖ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠦࠧᖗ"))
            return
        if not self.bstack1ll111111l1_opy_:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡂࠨᖘ") + str(str(self.bstack1ll1l1l11ll_opy_)) + bstack1lllll1l_opy_ (u"ࠨࠢᖙ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᖚ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠣࠤᖛ"))
            return
        instance = self.__1ll111l11ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡤࡶ࡬ࡹ࠽ࠣᖜ") + str(args) + bstack1lllll1l_opy_ (u"ࠥࠦᖝ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l1ll111l_opy_.bstack1ll11l11l1l_opy_ and test_hook_state == bstack1lll1lll111_opy_.PRE:
                bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack11l1ll1lll_opy_.value)
                name = str(EVENTS.bstack11l1ll1lll_opy_.name)+bstack1lllll1l_opy_ (u"ࠦ࠿ࠨᖞ")+str(test_framework_state.name)
                TestFramework.bstack1ll1l1l1lll_opy_(instance, name, bstack1ll111ll1l1_opy_)
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲࠡࡲࡵࡩ࠿ࠦࡻࡾࠤᖟ").format(e))
        try:
            if not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l11lll1_opy_) and test_hook_state == bstack1lll1lll111_opy_.PRE:
                test = bstack1l1l1ll111l_opy_.__1ll11lllll1_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡬ࡰࡣࡧࡩࡩࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᖠ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠢࠣᖡ"))
            if test_framework_state == bstack1llll111l1l_opy_.TEST:
                if test_hook_state == bstack1lll1lll111_opy_.PRE and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11l1lll1_opy_):
                    TestFramework.bstack1llll11ll1l_opy_(instance, TestFramework.bstack1ll11l1lll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡷࡹࡧࡲࡵࠢࡩࡳࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᖢ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠤࠥᖣ"))
                elif test_hook_state == bstack1lll1lll111_opy_.POST and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l11l1ll_opy_):
                    TestFramework.bstack1llll11ll1l_opy_(instance, TestFramework.bstack1ll1l11l1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲࡫࡮ࡥࠢࡩࡳࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᖤ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠦࠧᖥ"))
            elif test_framework_state == bstack1llll111l1l_opy_.LOG and test_hook_state == bstack1lll1lll111_opy_.POST:
                bstack1l1l1ll111l_opy_.__1ll111l1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll111_opy_.POST:
                self.__1ll1l1l1l1l_opy_(instance, *args)
                self.__1ll1l1l1111_opy_(instance)
            elif test_framework_state in bstack1l1l1ll111l_opy_.bstack1ll11l11l1l_opy_:
                self.__1ll11l1llll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᖦ") + str(instance.ref()) + bstack1lllll1l_opy_ (u"ࠨࠢᖧ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11111111_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l1ll111l_opy_.bstack1ll11l11l1l_opy_ and test_hook_state == bstack1lll1lll111_opy_.POST:
                name = str(EVENTS.bstack11l1ll1lll_opy_.name)+bstack1lllll1l_opy_ (u"ࠢ࠻ࠤᖨ")+str(test_framework_state.name)
                bstack1ll111ll1l1_opy_ = TestFramework.bstack1ll1l111lll_opy_(instance, name)
                bstack1llllllll1l_opy_.end(EVENTS.bstack11l1ll1lll_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᖩ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᖪ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᖫ").format(e))
    def bstack1l1lllll1ll_opy_(self):
        return self.bstack1ll111111l1_opy_
    def __1ll111ll111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1lllll1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣᖬ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11l111ll_opy_(rep, [bstack1lllll1l_opy_ (u"ࠧࡽࡨࡦࡰࠥᖭ"), bstack1lllll1l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᖮ"), bstack1lllll1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᖯ"), bstack1lllll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᖰ"), bstack1lllll1l_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠥᖱ"), bstack1lllll1l_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤᖲ")])
        return None
    def __1ll1l1l1l1l_opy_(self, instance: bstack1lll1l1llll_opy_, *args):
        result = self.__1ll111ll111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111l111_opy_ = None
        if result.get(bstack1lllll1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᖳ"), None) == bstack1lllll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧᖴ") and len(args) > 1 and getattr(args[1], bstack1lllll1l_opy_ (u"ࠨࡥࡹࡥ࡬ࡲ࡫ࡵࠢᖵ"), None) is not None:
            failure = [{bstack1lllll1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᖶ"): [args[1].excinfo.exconly(), result.get(bstack1lllll1l_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢᖷ"), None)]}]
            bstack111111l111_opy_ = bstack1lllll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᖸ") if bstack1lllll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨᖹ") in getattr(args[1].excinfo, bstack1lllll1l_opy_ (u"ࠦࡹࡿࡰࡦࡰࡤࡱࡪࠨᖺ"), bstack1lllll1l_opy_ (u"ࠧࠨᖻ")) else bstack1lllll1l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᖼ")
        bstack1ll11ll11l1_opy_ = result.get(bstack1lllll1l_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖽ"), TestFramework.bstack1l1llllll11_opy_)
        if bstack1ll11ll11l1_opy_ != TestFramework.bstack1l1llllll11_opy_:
            TestFramework.bstack1llll11ll1l_opy_(instance, TestFramework.bstack1ll11llll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1111l11l_opy_(instance, {
            TestFramework.bstack1lll11ll111_opy_: failure,
            TestFramework.bstack1l1llll11ll_opy_: bstack111111l111_opy_,
            TestFramework.bstack1lll1l1111l_opy_: bstack1ll11ll11l1_opy_,
        })
    def __1ll111l11ll_opy_(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll111l1l_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l11111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11llll1l_opy_ bstack1ll1111l1l1_opy_ this to be bstack1lllll1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᖾ")
            if test_framework_state == bstack1llll111l1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1llll1lll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1lllll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᖿ"), None), bstack1lllll1l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᗀ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1lllll1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᗁ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1llllllll_opy_(target) if target else None
        return instance
    def __1ll11l1llll_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l111111_opy_ = TestFramework.get_state(instance, bstack1l1l1ll111l_opy_.bstack1ll11l11ll1_opy_, {})
        if not key in bstack1ll1l111111_opy_:
            bstack1ll1l111111_opy_[key] = []
        bstack1ll1l1l111l_opy_ = TestFramework.get_state(instance, bstack1l1l1ll111l_opy_.bstack1l1llll1ll1_opy_, {})
        if not key in bstack1ll1l1l111l_opy_:
            bstack1ll1l1l111l_opy_[key] = []
        bstack1ll111ll11l_opy_ = {
            bstack1l1l1ll111l_opy_.bstack1ll11l11ll1_opy_: bstack1ll1l111111_opy_,
            bstack1l1l1ll111l_opy_.bstack1l1llll1ll1_opy_: bstack1ll1l1l111l_opy_,
        }
        if test_hook_state == bstack1lll1lll111_opy_.PRE:
            hook = {
                bstack1lllll1l_opy_ (u"ࠧࡱࡥࡺࠤᗂ"): key,
                TestFramework.bstack1ll11l1ll1l_opy_: uuid4().__str__(),
                TestFramework.bstack1l1llll1l11_opy_: TestFramework.bstack1l1llll1l1l_opy_,
                TestFramework.bstack1ll1l11l1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll111ll1ll_opy_: [],
                TestFramework.bstack1ll11lll111_opy_: args[1] if len(args) > 1 else bstack1lllll1l_opy_ (u"࠭ࠧᗃ"),
                TestFramework.bstack1ll11111l1l_opy_: bstack1ll1111ll11_opy_.bstack1ll11llllll_opy_()
            }
            bstack1ll1l111111_opy_[key].append(hook)
            bstack1ll111ll11l_opy_[bstack1l1l1ll111l_opy_.bstack1l1llll111l_opy_] = key
        elif test_hook_state == bstack1lll1lll111_opy_.POST:
            bstack1ll1111111l_opy_ = bstack1ll1l111111_opy_.get(key, [])
            hook = bstack1ll1111111l_opy_.pop() if bstack1ll1111111l_opy_ else None
            if hook:
                result = self.__1ll111ll111_opy_(*args)
                if result:
                    bstack1ll11l1l11l_opy_ = result.get(bstack1lllll1l_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᗄ"), TestFramework.bstack1l1llll1l1l_opy_)
                    if bstack1ll11l1l11l_opy_ != TestFramework.bstack1l1llll1l1l_opy_:
                        hook[TestFramework.bstack1l1llll1l11_opy_] = bstack1ll11l1l11l_opy_
                hook[TestFramework.bstack1ll1111lll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11111l1l_opy_]= bstack1ll1111ll11_opy_.bstack1ll11llllll_opy_()
                self.bstack1ll11ll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l11111_opy_, [])
                if logs: self.bstack1ll111l1111_opy_(instance, logs)
                bstack1ll1l1l111l_opy_[key].append(hook)
                bstack1ll111ll11l_opy_[bstack1l1l1ll111l_opy_.bstack1ll111l1l11_opy_] = key
        TestFramework.bstack1ll1111l11l_opy_(instance, bstack1ll111ll11l_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡩࡱࡲ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼ࡭ࡨࡽࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࡀࡿ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࢁࠥ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡃࠢᗅ") + str(bstack1ll1l1l111l_opy_) + bstack1lllll1l_opy_ (u"ࠤࠥᗆ"))
    def __1ll1l11111l_opy_(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11l111ll_opy_(args[0], [bstack1lllll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᗇ"), bstack1lllll1l_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧᗈ"), bstack1lllll1l_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᗉ"), bstack1lllll1l_opy_ (u"ࠨࡩࡥࡵࠥᗊ"), bstack1lllll1l_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤᗋ"), bstack1lllll1l_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣᗌ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1lllll1l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᗍ")) else fixturedef.get(bstack1lllll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᗎ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1lllll1l_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࠤᗏ")) else None
        node = request.node if hasattr(request, bstack1lllll1l_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᗐ")) else None
        target = request.node.nodeid if hasattr(node, bstack1lllll1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᗑ")) else None
        baseid = fixturedef.get(bstack1lllll1l_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢᗒ"), None) or bstack1lllll1l_opy_ (u"ࠣࠤᗓ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1lllll1l_opy_ (u"ࠤࡢࡴࡾ࡬ࡵ࡯ࡥ࡬ࡸࡪࡳࠢᗔ")):
            target = bstack1l1l1ll111l_opy_.__1ll111lll1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1lllll1l_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᗕ")) else None
            if target and not TestFramework.bstack1l1llllllll_opy_(target):
                self.__1l1llll1lll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦ࡮ࡰࡦࡨࡁࢀࡴ࡯ࡥࡧࢀࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࠨᗖ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠧࠨᗗ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦᗘ") + str(target) + bstack1lllll1l_opy_ (u"ࠢࠣᗙ"))
            return None
        instance = TestFramework.bstack1l1llllllll_opy_(target)
        if not instance:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡣࡣࡶࡩ࡮ࡪ࠽ࡼࡤࡤࡷࡪ࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥᗚ") + str(target) + bstack1lllll1l_opy_ (u"ࠤࠥᗛ"))
            return None
        bstack1ll1l11ll11_opy_ = TestFramework.get_state(instance, bstack1l1l1ll111l_opy_.bstack1ll1l111ll1_opy_, {})
        if os.getenv(bstack1lllll1l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡉࡍ࡝࡚ࡕࡓࡇࡖࠦᗜ"), bstack1lllll1l_opy_ (u"ࠦ࠶ࠨᗝ")) == bstack1lllll1l_opy_ (u"ࠧ࠷ࠢᗞ"):
            bstack1l1lllll1l1_opy_ = bstack1lllll1l_opy_ (u"ࠨ࠺ࠣᗟ").join((scope, fixturename))
            bstack1l1lll1ll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l1111ll_opy_ = {
                bstack1lllll1l_opy_ (u"ࠢ࡬ࡧࡼࠦᗠ"): bstack1l1lllll1l1_opy_,
                bstack1lllll1l_opy_ (u"ࠣࡶࡤ࡫ࡸࠨᗡ"): bstack1l1l1ll111l_opy_.__1ll1l1ll111_opy_(request.node),
                bstack1lllll1l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࠥᗢ"): fixturedef,
                bstack1lllll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᗣ"): scope,
                bstack1lllll1l_opy_ (u"ࠦࡹࡿࡰࡦࠤᗤ"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll111_opy_.POST and callable(getattr(args[-1], bstack1lllll1l_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᗥ"), None)):
                    bstack1ll1l1111ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡴࡺࡲࡨࠦᗦ")] = TestFramework.bstack1ll11ll1l1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll111_opy_.PRE:
                bstack1ll1l1111ll_opy_[bstack1lllll1l_opy_ (u"ࠢࡶࡷ࡬ࡨࠧᗧ")] = uuid4().__str__()
                bstack1ll1l1111ll_opy_[bstack1l1l1ll111l_opy_.bstack1ll1l11l1l1_opy_] = bstack1l1lll1ll1l_opy_
            elif test_hook_state == bstack1lll1lll111_opy_.POST:
                bstack1ll1l1111ll_opy_[bstack1l1l1ll111l_opy_.bstack1ll1111lll1_opy_] = bstack1l1lll1ll1l_opy_
            if bstack1l1lllll1l1_opy_ in bstack1ll1l11ll11_opy_:
                bstack1ll1l11ll11_opy_[bstack1l1lllll1l1_opy_].update(bstack1ll1l1111ll_opy_)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࠾ࠤᗨ") + str(bstack1ll1l11ll11_opy_[bstack1l1lllll1l1_opy_]) + bstack1lllll1l_opy_ (u"ࠤࠥᗩ"))
            else:
                bstack1ll1l11ll11_opy_[bstack1l1lllll1l1_opy_] = bstack1ll1l1111ll_opy_
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡾࠢࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࠨᗪ") + str(len(bstack1ll1l11ll11_opy_)) + bstack1lllll1l_opy_ (u"ࠦࠧᗫ"))
        TestFramework.bstack1llll11ll1l_opy_(instance, bstack1l1l1ll111l_opy_.bstack1ll1l111ll1_opy_, bstack1ll1l11ll11_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࡻ࡭ࡧࡱࠬࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠩࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᗬ") + str(instance.ref()) + bstack1lllll1l_opy_ (u"ࠨࠢᗭ"))
        return instance
    def __1l1llll1lll_opy_(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        ob = bstack1lll1l1llll_opy_(ctx, self.bstack1ll1l1l11ll_opy_, self.bstack1ll111llll1_opy_, test_framework_state)
        TestFramework.bstack1ll1111l11l_opy_(ob, {
            TestFramework.bstack1lll1l111l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll11lll11_opy_: context.test_framework_version,
            TestFramework.bstack1ll111lllll_opy_: [],
            bstack1l1l1ll111l_opy_.bstack1ll1l111ll1_opy_: {},
            bstack1l1l1ll111l_opy_.bstack1l1llll1ll1_opy_: {},
            bstack1l1l1ll111l_opy_.bstack1ll11l11ll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll11ll1l_opy_(ob, TestFramework.bstack1ll1111l111_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll11ll1l_opy_(ob, TestFramework.bstack1llllllllll_opy_, context.platform_index)
        TestFramework.bstack1lll11lllll_opy_[ctx.id] = ob
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡥࡷࡼ࠳࡯ࡤ࠾ࡽࡦࡸࡽ࠴ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢᗮ") + str(TestFramework.bstack1lll11lllll_opy_.keys()) + bstack1lllll1l_opy_ (u"ࠣࠤᗯ"))
        return ob
    def bstack1ll11ll1ll1_opy_(self, instance: bstack1lll1l1llll_opy_, bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_]):
        bstack1ll11111lll_opy_ = (
            bstack1l1l1ll111l_opy_.bstack1l1llll111l_opy_
            if bstack1llll1l1lll_opy_[1] == bstack1lll1lll111_opy_.PRE
            else bstack1l1l1ll111l_opy_.bstack1ll111l1l11_opy_
        )
        hook = bstack1l1l1ll111l_opy_.bstack1l1lllll111_opy_(instance, bstack1ll11111lll_opy_)
        entries = hook.get(TestFramework.bstack1ll111ll1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll111lllll_opy_, []))
        return entries
    def bstack1l1llll11l1_opy_(self, instance: bstack1lll1l1llll_opy_, bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_]):
        bstack1ll11111lll_opy_ = (
            bstack1l1l1ll111l_opy_.bstack1l1llll111l_opy_
            if bstack1llll1l1lll_opy_[1] == bstack1lll1lll111_opy_.PRE
            else bstack1l1l1ll111l_opy_.bstack1ll111l1l11_opy_
        )
        bstack1l1l1ll111l_opy_.bstack1l1llllll1l_opy_(instance, bstack1ll11111lll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll111lllll_opy_, []).clear()
    def bstack1ll11ll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1lllll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡴ࡫ࡰ࡭ࡱࡧࡲࠡࡶࡲࠤࡹ࡮ࡥࠡࡌࡤࡺࡦࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡃࡩࡧࡦ࡯ࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡬ࡲࡸ࡯ࡤࡦࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠳࡚ࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡵࡩࡵࡲࡡࡤࡧࡶࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦࠥ࡯࡮ࠡ࡫ࡷࡷࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡌࡪࠥࡧࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡯ࡤࡸࡨ࡮ࡥࡴࠢࡤࠤࡲࡵࡤࡪࡨ࡬ࡩࡩࠦࡨࡰࡱ࡮࠱ࡱ࡫ࡶࡦ࡮ࠣࡪ࡮ࡲࡥ࠭ࠢ࡬ࡸࠥࡩࡲࡦࡣࡷࡩࡸࠦࡡࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࠣࡻ࡮ࡺࡨࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡙ࠥࡩ࡮࡫࡯ࡥࡷࡲࡹ࠭ࠢ࡬ࡸࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡴࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡥࡽࠥࡸࡥࡱ࡮ࡤࡧ࡮ࡴࡧࠡࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡖ࡫ࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡤࡶࡪࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥ࡮࡯ࡰ࡭ࠪࡷࠥࠨ࡬ࡰࡩࡶࠦࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࠺ࠡࡖ࡫ࡩࠥ࡫ࡶࡦࡰࡷࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷࠥࡧ࡮ࡥࠢ࡫ࡳࡴࡱࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡘࡪࡹࡴࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᗰ")
        global _1ll111l11l1_opy_
        platform_index = os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᗱ")]
        bstack1ll1l11l11l_opy_ = os.path.join(bstack1ll11ll1111_opy_, (bstack1ll11lll11l_opy_ + str(platform_index)), bstack11llll111l1_opy_)
        if not os.path.exists(bstack1ll1l11l11l_opy_) or not os.path.isdir(bstack1ll1l11l11l_opy_):
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴࡴࠢࡷࡳࠥࡶࡲࡰࡥࡨࡷࡸࠦࡻࡾࠤᗲ").format(bstack1ll1l11l11l_opy_))
            return
        logs = hook.get(bstack1lllll1l_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᗳ"), [])
        with os.scandir(bstack1ll1l11l11l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll111l11l1_opy_:
                    self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦᗴ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1lllll1l_opy_ (u"ࠢࠣᗵ")
                    log_entry = bstack1ll1l1l1ll1_opy_(
                        kind=bstack1lllll1l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᗶ"),
                        message=bstack1lllll1l_opy_ (u"ࠤࠥᗷ"),
                        level=bstack1lllll1l_opy_ (u"ࠥࠦᗸ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l1l111_opy_=entry.stat().st_size,
                        bstack1ll1l1l11l1_opy_=bstack1lllll1l_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᗹ"),
                        bstack111l1l1_opy_=os.path.abspath(entry.path),
                        bstack1ll11111l11_opy_=hook.get(TestFramework.bstack1ll11l1ll1l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll111l11l1_opy_.add(abs_path)
        platform_index = os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᗺ")]
        bstack1ll1l1111l1_opy_ = os.path.join(bstack1ll11ll1111_opy_, (bstack1ll11lll11l_opy_ + str(platform_index)), bstack11llll111l1_opy_, bstack11llll1111l_opy_)
        if not os.path.exists(bstack1ll1l1111l1_opy_) or not os.path.isdir(bstack1ll1l1111l1_opy_):
            self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡎࡰࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡩࡳࡺࡴࡤࠡࡣࡷ࠾ࠥࢁࡽࠣᗻ").format(bstack1ll1l1111l1_opy_))
        else:
            self.logger.info(bstack1lllll1l_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡨࡵࡳࡲࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠼ࠣࡿࢂࠨᗼ").format(bstack1ll1l1111l1_opy_))
            with os.scandir(bstack1ll1l1111l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll111l11l1_opy_:
                        self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᗽ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1lllll1l_opy_ (u"ࠤࠥᗾ")
                        log_entry = bstack1ll1l1l1ll1_opy_(
                            kind=bstack1lllll1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᗿ"),
                            message=bstack1lllll1l_opy_ (u"ࠦࠧᘀ"),
                            level=bstack1lllll1l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᘁ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l1l111_opy_=entry.stat().st_size,
                            bstack1ll1l1l11l1_opy_=bstack1lllll1l_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᘂ"),
                            bstack111l1l1_opy_=os.path.abspath(entry.path),
                            bstack1l1lllllll1_opy_=hook.get(TestFramework.bstack1ll11l1ll1l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll111l11l1_opy_.add(abs_path)
        hook[bstack1lllll1l_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᘃ")] = logs
    def bstack1ll111l1111_opy_(
        self,
        bstack1ll11ll11ll_opy_: bstack1lll1l1llll_opy_,
        entries: List[bstack1ll1l1l1ll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1lllll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧᘄ"))
        req.platform_index = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1llllllllll_opy_)
        req.execution_context.hash = str(bstack1ll11ll11ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll11ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll11ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll1l111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll11lll11_opy_)
            log_entry.uuid = entry.bstack1ll11111l11_opy_
            log_entry.test_framework_state = bstack1ll11ll11ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lllll1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᘅ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1lllll1l_opy_ (u"ࠥࠦᘆ")
            if entry.kind == bstack1lllll1l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᘇ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1l111_opy_
                log_entry.file_path = entry.bstack111l1l1_opy_
        def bstack1ll111lll11_opy_():
            bstack1ll111ll1_opy_ = datetime.now()
            try:
                self.bstack1lllllll111_opy_.LogCreatedEvent(req)
                bstack1ll11ll11ll_opy_.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤᘈ"), datetime.now() - bstack1ll111ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡾࢁࠧᘉ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l11_opy_.enqueue(bstack1ll111lll11_opy_)
    def __1ll1l1l1111_opy_(self, instance) -> None:
        bstack1lllll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡑࡵࡡࡥࡵࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡦ࡭ࡳࠡࡨࡲࡶࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡳࡧࡤࡸࡪࡹࠠࡢࠢࡧ࡭ࡨࡺࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡹ࡫ࡳࡵࠢ࡯ࡩࡻ࡫࡬ࠡࡥࡸࡷࡹࡵ࡭ࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡦࡳࡱࡰࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡵࡴࡶࡲࡱ࡙ࡧࡧࡎࡣࡱࡥ࡬࡫ࡲࠡࡣࡱࡨࠥࡻࡰࡥࡣࡷࡩࡸࠦࡴࡩࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡹࡴࡢࡶࡨࠤࡺࡹࡩ࡯ࡩࠣࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᘊ")
        bstack1ll111ll11l_opy_ = {bstack1lllll1l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠥᘋ"): bstack1ll1111ll11_opy_.bstack1ll11llllll_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll1111l11l_opy_(instance, bstack1ll111ll11l_opy_)
    @staticmethod
    def bstack1l1lllll111_opy_(instance: bstack1lll1l1llll_opy_, bstack1ll11111lll_opy_: str):
        bstack1ll1l11l111_opy_ = (
            bstack1l1l1ll111l_opy_.bstack1l1llll1ll1_opy_
            if bstack1ll11111lll_opy_ == bstack1l1l1ll111l_opy_.bstack1ll111l1l11_opy_
            else bstack1l1l1ll111l_opy_.bstack1ll11l11ll1_opy_
        )
        bstack1ll11111ll1_opy_ = TestFramework.get_state(instance, bstack1ll11111lll_opy_, None)
        bstack1l1lllll11l_opy_ = TestFramework.get_state(instance, bstack1ll1l11l111_opy_, None) if bstack1ll11111ll1_opy_ else None
        return (
            bstack1l1lllll11l_opy_[bstack1ll11111ll1_opy_][-1]
            if isinstance(bstack1l1lllll11l_opy_, dict) and len(bstack1l1lllll11l_opy_.get(bstack1ll11111ll1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l1llllll1l_opy_(instance: bstack1lll1l1llll_opy_, bstack1ll11111lll_opy_: str):
        hook = bstack1l1l1ll111l_opy_.bstack1l1lllll111_opy_(instance, bstack1ll11111lll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll111ll1ll_opy_, []).clear()
    @staticmethod
    def __1ll111l1ll1_opy_(instance: bstack1lll1l1llll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1lllll1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡥࡲࡶࡩࡹࠢᘌ"), None)):
            return
        if os.getenv(bstack1lllll1l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡏࡓࡌ࡙ࠢᘍ"), bstack1lllll1l_opy_ (u"ࠦ࠶ࠨᘎ")) != bstack1lllll1l_opy_ (u"ࠧ࠷ࠢᘏ"):
            bstack1l1l1ll111l_opy_.logger.warning(bstack1lllll1l_opy_ (u"ࠨࡩࡨࡰࡲࡶ࡮ࡴࡧࠡࡥࡤࡴࡱࡵࡧࠣᘐ"))
            return
        bstack1ll1111ll1l_opy_ = {
            bstack1lllll1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᘑ"): (bstack1l1l1ll111l_opy_.bstack1l1llll111l_opy_, bstack1l1l1ll111l_opy_.bstack1ll11l11ll1_opy_),
            bstack1lllll1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᘒ"): (bstack1l1l1ll111l_opy_.bstack1ll111l1l11_opy_, bstack1l1l1ll111l_opy_.bstack1l1llll1ll1_opy_),
        }
        for when in (bstack1lllll1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᘓ"), bstack1lllll1l_opy_ (u"ࠥࡧࡦࡲ࡬ࠣᘔ"), bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᘕ")):
            bstack1ll1l1ll1l1_opy_ = args[1].get_records(when)
            if not bstack1ll1l1ll1l1_opy_:
                continue
            records = [
                bstack1ll1l1l1ll1_opy_(
                    kind=TestFramework.bstack1ll1l111l1l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1lllll1l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠣᘖ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1lllll1l_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪࠢᘗ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l1ll1l1_opy_
                if isinstance(getattr(r, bstack1lllll1l_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣᘘ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1l111l11_opy_, bstack1ll1l11l111_opy_ = bstack1ll1111ll1l_opy_.get(when, (None, None))
            bstack1ll11lll1ll_opy_ = TestFramework.get_state(instance, bstack1ll1l111l11_opy_, None) if bstack1ll1l111l11_opy_ else None
            bstack1l1lllll11l_opy_ = TestFramework.get_state(instance, bstack1ll1l11l111_opy_, None) if bstack1ll11lll1ll_opy_ else None
            if isinstance(bstack1l1lllll11l_opy_, dict) and len(bstack1l1lllll11l_opy_.get(bstack1ll11lll1ll_opy_, [])) > 0:
                hook = bstack1l1lllll11l_opy_[bstack1ll11lll1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll111ll1ll_opy_ in hook:
                    hook[TestFramework.bstack1ll111ll1ll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll111lllll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11lllll1_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l1ll111l_opy_.__1ll111lll1l_opy_(test.location) if hasattr(test, bstack1lllll1l_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥᘙ")) else getattr(test, bstack1lllll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᘚ"), None)
        test_name = test.name if hasattr(test, bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᘛ")) else None
        bstack1ll111l1lll_opy_ = test.fspath.strpath if hasattr(test, bstack1lllll1l_opy_ (u"ࠦ࡫ࡹࡰࡢࡶ࡫ࠦᘜ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll111l1lll_opy_:
            return None
        code = None
        if hasattr(test, bstack1lllll1l_opy_ (u"ࠧࡵࡢ࡫ࠤᘝ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll111ll_opy_ = []
        try:
            bstack11llll111ll_opy_ = bstack1ll11l1l_opy_.bstack1ll11111_opy_(test)
        except:
            bstack1l1l1ll111l_opy_.logger.warning(bstack1lllll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡧࡶࡸࠥࡹࡣࡰࡲࡨࡷ࠱ࠦࡴࡦࡵࡷࠤࡸࡩ࡯ࡱࡧࡶࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡸࡥࡴࡱ࡯ࡺࡪࡪࠠࡪࡰࠣࡇࡑࡏࠢᘞ"))
        return {
            TestFramework.bstack1lll1lll1ll_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11lll1_opy_: test_id,
            TestFramework.bstack1ll111l111l_opy_: test_name,
            TestFramework.bstack1ll11l1l1l1_opy_: getattr(test, bstack1lllll1l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᘟ"), None),
            TestFramework.bstack1ll11l11lll_opy_: bstack1ll111l1lll_opy_,
            TestFramework.bstack1ll11l1111l_opy_: bstack1l1l1ll111l_opy_.__1ll1l1ll111_opy_(test),
            TestFramework.bstack1ll1111llll_opy_: code,
            TestFramework.bstack1lll1l1111l_opy_: TestFramework.bstack1l1llllll11_opy_,
            TestFramework.bstack1lll111l11l_opy_: test_id,
            TestFramework.bstack1l11111l1ll_opy_: bstack11llll111ll_opy_
        }
    @staticmethod
    def __1ll1l1ll111_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1lllll1l_opy_ (u"ࠣࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸࠨᘠ"), [])
            markers.extend([getattr(m, bstack1lllll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᘡ"), None) for m in own_markers if getattr(m, bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᘢ"), None)])
            current = getattr(current, bstack1lllll1l_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᘣ"), None)
        return markers
    @staticmethod
    def __1ll111lll1l_opy_(location):
        return bstack1lllll1l_opy_ (u"ࠧࡀ࠺ࠣᘤ").join(filter(lambda x: isinstance(x, str), location))