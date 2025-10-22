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
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lllll1l_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1111ll_opy_ import bstack1l1lllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1llll_opy_,
    bstack1lll1l1ll11_opy_,
    bstack1lll11lll1l_opy_,
    bstack1ll111l1111_opy_,
    bstack1ll1l1111l1_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll11111111_opy_
from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l11ll_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l1l1ll1_opy_ import bstack1ll11llll11_opy_
from bstack_utils.bstack1lll11ll_opy_ import bstack1l1l11ll_opy_
bstack1ll11111l1l_opy_ = bstack1ll11111111_opy_()
bstack1ll11llll1l_opy_ = 1.0
bstack1ll11l111l1_opy_ = bstack11l1l11_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᖆ")
bstack11llll1111l_opy_ = bstack11l1l11_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᖇ")
bstack11lll1llll1_opy_ = bstack11l1l11_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᖈ")
bstack11llll111l1_opy_ = bstack11l1l11_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢᖉ")
bstack11llll11111_opy_ = bstack11l1l11_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦᖊ")
_1ll1l111ll1_opy_ = set()
class bstack1l11llll1l1_opy_(TestFramework):
    bstack1ll1111ll1l_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᖋ")
    bstack1ll1l1111ll_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧᖌ")
    bstack1ll11111l11_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᖍ")
    bstack1ll1l1l111l_opy_ = bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦᖎ")
    bstack1ll111ll1ll_opy_ = bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᖏ")
    bstack1ll11l1l1ll_opy_: bool
    bstack1lll11l11ll_opy_: bstack1lll11l11l1_opy_  = None
    bstack1llllllll11_opy_ = None
    bstack1ll11l11111_opy_ = [
        bstack1lll1l1llll_opy_.BEFORE_ALL,
        bstack1lll1l1llll_opy_.AFTER_ALL,
        bstack1lll1l1llll_opy_.BEFORE_EACH,
        bstack1lll1l1llll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l1lll1l1ll_opy_: Dict[str, str],
        bstack1l1lll1ll11_opy_: List[str]=[bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᖐ")],
        bstack1lll11l11ll_opy_: bstack1lll11l11l1_opy_=None,
        bstack1llllllll11_opy_=None
    ):
        super().__init__(bstack1l1lll1ll11_opy_, bstack1l1lll1l1ll_opy_, bstack1lll11l11ll_opy_)
        self.bstack1ll11l1l1ll_opy_ = any(bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᖑ") in item.lower() for item in bstack1l1lll1ll11_opy_)
        self.bstack1llllllll11_opy_ = bstack1llllllll11_opy_
    def track_event(
        self,
        context: bstack1ll111l1111_opy_,
        test_framework_state: bstack1lll1l1llll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1llll_opy_.TEST or test_framework_state in bstack1l11llll1l1_opy_.bstack1ll11l11111_opy_:
            bstack1l1lllll1l1_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1llll_opy_.NONE:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢᖒ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠢࠣᖓ"))
            return
        if not self.bstack1ll11l1l1ll_opy_:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤᖔ") + str(str(self.bstack1l1lll1ll11_opy_)) + bstack11l1l11_opy_ (u"ࠤࠥᖕ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᖖ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠦࠧᖗ"))
            return
        instance = self.__1ll11lllll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦᖘ") + str(args) + bstack11l1l11_opy_ (u"ࠨࠢᖙ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11llll1l1_opy_.bstack1ll11l11111_opy_ and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack1ll1l11l111_opy_(EVENTS.bstack1ll1111ll1_opy_.value)
                name = str(EVENTS.bstack1ll1111ll1_opy_.name)+bstack11l1l11_opy_ (u"ࠢ࠻ࠤᖚ")+str(test_framework_state.name)
                TestFramework.bstack1l1llll11l1_opy_(instance, name, bstack1ll1l11llll_opy_)
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧᖛ").format(e))
        try:
            if not TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1ll1111llll_opy_) and test_hook_state == bstack1lll11lll1l_opy_.PRE:
                test = bstack1l11llll1l1_opy_.__1l1lllll111_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖜ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠥࠦᖝ"))
            if test_framework_state == bstack1lll1l1llll_opy_.TEST:
                if test_hook_state == bstack1lll11lll1l_opy_.PRE and not TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1ll11lll11l_opy_):
                    TestFramework.bstack1llllll1l11_opy_(instance, TestFramework.bstack1ll11lll11l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖞ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠧࠨᖟ"))
                elif test_hook_state == bstack1lll11lll1l_opy_.POST and not TestFramework.bstack111111111l_opy_(instance, TestFramework.bstack1ll1l11l1ll_opy_):
                    TestFramework.bstack1llllll1l11_opy_(instance, TestFramework.bstack1ll1l11l1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖠ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠢࠣᖡ"))
            elif test_framework_state == bstack1lll1l1llll_opy_.LOG and test_hook_state == bstack1lll11lll1l_opy_.POST:
                bstack1l11llll1l1_opy_.__1ll111l1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1llll_opy_.LOG_REPORT and test_hook_state == bstack1lll11lll1l_opy_.POST:
                self.__1ll111l111l_opy_(instance, *args)
                self.__1ll1l1l1lll_opy_(instance)
            elif test_framework_state in bstack1l11llll1l1_opy_.bstack1ll11l11111_opy_:
                self.__1l1llll11ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᖢ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠤࠥᖣ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11l1lll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11llll1l1_opy_.bstack1ll11l11111_opy_ and test_hook_state == bstack1lll11lll1l_opy_.POST:
                name = str(EVENTS.bstack1ll1111ll1_opy_.name)+bstack11l1l11_opy_ (u"ࠥ࠾ࠧᖤ")+str(test_framework_state.name)
                bstack1ll1l11llll_opy_ = TestFramework.bstack1ll1l11ll11_opy_(instance, name)
                bstack1llllll1ll1_opy_.end(EVENTS.bstack1ll1111ll1_opy_.value, bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᖥ"), bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᖦ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᖧ").format(e))
    def bstack1l1llll1111_opy_(self):
        return self.bstack1ll11l1l1ll_opy_
    def __1l1llll1ll1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l1l11_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᖨ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l11lll1_opy_(rep, [bstack11l1l11_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᖩ"), bstack11l1l11_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖪ"), bstack11l1l11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᖫ"), bstack11l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᖬ"), bstack11l1l11_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨᖭ"), bstack11l1l11_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᖮ")])
        return None
    def __1ll111l111l_opy_(self, instance: bstack1lll1l1ll11_opy_, *args):
        result = self.__1l1llll1ll1_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111l1l_opy_ = None
        if result.get(bstack11l1l11_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖯ"), None) == bstack11l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᖰ") and len(args) > 1 and getattr(args[1], bstack11l1l11_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥᖱ"), None) is not None:
            failure = [{bstack11l1l11_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᖲ"): [args[1].excinfo.exconly(), result.get(bstack11l1l11_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥᖳ"), None)]}]
            bstack1111111l1l_opy_ = bstack11l1l11_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᖴ") if bstack11l1l11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᖵ") in getattr(args[1].excinfo, bstack11l1l11_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤᖶ"), bstack11l1l11_opy_ (u"ࠣࠤᖷ")) else bstack11l1l11_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᖸ")
        bstack1ll111llll1_opy_ = result.get(bstack11l1l11_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖹ"), TestFramework.bstack1ll11ll11l1_opy_)
        if bstack1ll111llll1_opy_ != TestFramework.bstack1ll11ll11l1_opy_:
            TestFramework.bstack1llllll1l11_opy_(instance, TestFramework.bstack1ll11111ll1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11ll1ll1_opy_(instance, {
            TestFramework.bstack1lll1llll11_opy_: failure,
            TestFramework.bstack1ll11l1l111_opy_: bstack1111111l1l_opy_,
            TestFramework.bstack1lll11l1l1l_opy_: bstack1ll111llll1_opy_,
        })
    def __1ll11lllll1_opy_(
        self,
        context: bstack1ll111l1111_opy_,
        test_framework_state: bstack1lll1l1llll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1llll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11lll1ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll111ll111_opy_ bstack1ll11ll111l_opy_ this to be bstack11l1l11_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᖺ")
            if test_framework_state == bstack1lll1l1llll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11l1l1l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1llll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᖻ"), None), bstack11l1l11_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖼ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l1l11_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᖽ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1lll1l1l1_opy_(target) if target else None
        return instance
    def __1l1llll11ll_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        test_framework_state: bstack1lll1l1llll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1llll111l_opy_ = TestFramework.get_state(instance, bstack1l11llll1l1_opy_.bstack1ll1l1111ll_opy_, {})
        if not key in bstack1l1llll111l_opy_:
            bstack1l1llll111l_opy_[key] = []
        bstack1ll11ll11ll_opy_ = TestFramework.get_state(instance, bstack1l11llll1l1_opy_.bstack1ll11111l11_opy_, {})
        if not key in bstack1ll11ll11ll_opy_:
            bstack1ll11ll11ll_opy_[key] = []
        bstack1ll11ll1lll_opy_ = {
            bstack1l11llll1l1_opy_.bstack1ll1l1111ll_opy_: bstack1l1llll111l_opy_,
            bstack1l11llll1l1_opy_.bstack1ll11111l11_opy_: bstack1ll11ll11ll_opy_,
        }
        if test_hook_state == bstack1lll11lll1l_opy_.PRE:
            hook = {
                bstack11l1l11_opy_ (u"ࠣ࡭ࡨࡽࠧᖾ"): key,
                TestFramework.bstack1ll111ll11l_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l111l11_opy_: TestFramework.bstack1ll1111111l_opy_,
                TestFramework.bstack1l1llll1lll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1lllll11l_opy_: [],
                TestFramework.bstack1ll111ll1l1_opy_: args[1] if len(args) > 1 else bstack11l1l11_opy_ (u"ࠩࠪᖿ"),
                TestFramework.bstack1ll11lll1l1_opy_: bstack1ll11llll11_opy_.bstack1ll11llllll_opy_()
            }
            bstack1l1llll111l_opy_[key].append(hook)
            bstack1ll11ll1lll_opy_[bstack1l11llll1l1_opy_.bstack1ll1l1l111l_opy_] = key
        elif test_hook_state == bstack1lll11lll1l_opy_.POST:
            bstack1ll1111l111_opy_ = bstack1l1llll111l_opy_.get(key, [])
            hook = bstack1ll1111l111_opy_.pop() if bstack1ll1111l111_opy_ else None
            if hook:
                result = self.__1l1llll1ll1_opy_(*args)
                if result:
                    bstack1ll111l1lll_opy_ = result.get(bstack11l1l11_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᗀ"), TestFramework.bstack1ll1111111l_opy_)
                    if bstack1ll111l1lll_opy_ != TestFramework.bstack1ll1111111l_opy_:
                        hook[TestFramework.bstack1ll1l111l11_opy_] = bstack1ll111l1lll_opy_
                hook[TestFramework.bstack1ll1l1l1l1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11lll1l1_opy_]= bstack1ll11llll11_opy_.bstack1ll11llllll_opy_()
                self.bstack1l1llll1l11_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l1ll11_opy_, [])
                if logs: self.bstack1ll1l111l1l_opy_(instance, logs)
                bstack1ll11ll11ll_opy_[key].append(hook)
                bstack1ll11ll1lll_opy_[bstack1l11llll1l1_opy_.bstack1ll111ll1ll_opy_] = key
        TestFramework.bstack1ll11ll1ll1_opy_(instance, bstack1ll11ll1lll_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥᗁ") + str(bstack1ll11ll11ll_opy_) + bstack11l1l11_opy_ (u"ࠧࠨᗂ"))
    def __1ll11lll1ll_opy_(
        self,
        context: bstack1ll111l1111_opy_,
        test_framework_state: bstack1lll1l1llll_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l11lll1_opy_(args[0], [bstack11l1l11_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗃ"), bstack11l1l11_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᗄ"), bstack11l1l11_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᗅ"), bstack11l1l11_opy_ (u"ࠤ࡬ࡨࡸࠨᗆ"), bstack11l1l11_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᗇ"), bstack11l1l11_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦᗈ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11l1l11_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗉ")) else fixturedef.get(bstack11l1l11_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗊ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l1l11_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧᗋ")) else None
        node = request.node if hasattr(request, bstack11l1l11_opy_ (u"ࠣࡰࡲࡨࡪࠨᗌ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l1l11_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᗍ")) else None
        baseid = fixturedef.get(bstack11l1l11_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᗎ"), None) or bstack11l1l11_opy_ (u"ࠦࠧᗏ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l1l11_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥᗐ")):
            target = bstack1l11llll1l1_opy_.__1ll11ll1l11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l1l11_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᗑ")) else None
            if target and not TestFramework.bstack1l1lll1l1l1_opy_(target):
                self.__1ll11l1l1l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᗒ") + str(test_hook_state) + bstack11l1l11_opy_ (u"ࠣࠤᗓ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢᗔ") + str(target) + bstack11l1l11_opy_ (u"ࠥࠦᗕ"))
            return None
        instance = TestFramework.bstack1l1lll1l1l1_opy_(target)
        if not instance:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᗖ") + str(target) + bstack11l1l11_opy_ (u"ࠧࠨᗗ"))
            return None
        bstack1ll1l1l1111_opy_ = TestFramework.get_state(instance, bstack1l11llll1l1_opy_.bstack1ll1111ll1l_opy_, {})
        if os.getenv(bstack11l1l11_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢᗘ"), bstack11l1l11_opy_ (u"ࠢ࠲ࠤᗙ")) == bstack11l1l11_opy_ (u"ࠣ࠳ࠥᗚ"):
            bstack1ll1l1l11l1_opy_ = bstack11l1l11_opy_ (u"ࠤ࠽ࠦᗛ").join((scope, fixturename))
            bstack1ll111l11ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l11l11l_opy_ = {
                bstack11l1l11_opy_ (u"ࠥ࡯ࡪࡿࠢᗜ"): bstack1ll1l1l11l1_opy_,
                bstack11l1l11_opy_ (u"ࠦࡹࡧࡧࡴࠤᗝ"): bstack1l11llll1l1_opy_.__1l1llllll11_opy_(request.node),
                bstack11l1l11_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨᗞ"): fixturedef,
                bstack11l1l11_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗟ"): scope,
                bstack11l1l11_opy_ (u"ࠢࡵࡻࡳࡩࠧᗠ"): None,
            }
            try:
                if test_hook_state == bstack1lll11lll1l_opy_.POST and callable(getattr(args[-1], bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᗡ"), None)):
                    bstack1ll1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᗢ")] = TestFramework.bstack1ll1111l1ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11lll1l_opy_.PRE:
                bstack1ll1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᗣ")] = uuid4().__str__()
                bstack1ll1l11l11l_opy_[bstack1l11llll1l1_opy_.bstack1l1llll1lll_opy_] = bstack1ll111l11ll_opy_
            elif test_hook_state == bstack1lll11lll1l_opy_.POST:
                bstack1ll1l11l11l_opy_[bstack1l11llll1l1_opy_.bstack1ll1l1l1l1l_opy_] = bstack1ll111l11ll_opy_
            if bstack1ll1l1l11l1_opy_ in bstack1ll1l1l1111_opy_:
                bstack1ll1l1l1111_opy_[bstack1ll1l1l11l1_opy_].update(bstack1ll1l11l11l_opy_)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧᗤ") + str(bstack1ll1l1l1111_opy_[bstack1ll1l1l11l1_opy_]) + bstack11l1l11_opy_ (u"ࠧࠨᗥ"))
            else:
                bstack1ll1l1l1111_opy_[bstack1ll1l1l11l1_opy_] = bstack1ll1l11l11l_opy_
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤᗦ") + str(len(bstack1ll1l1l1111_opy_)) + bstack11l1l11_opy_ (u"ࠢࠣᗧ"))
        TestFramework.bstack1llllll1l11_opy_(instance, bstack1l11llll1l1_opy_.bstack1ll1111ll1l_opy_, bstack1ll1l1l1111_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᗨ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠤࠥᗩ"))
        return instance
    def __1ll11l1l1l1_opy_(
        self,
        context: bstack1ll111l1111_opy_,
        test_framework_state: bstack1lll1l1llll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll111ll_opy_.create_context(target)
        ob = bstack1lll1l1ll11_opy_(ctx, self.bstack1l1lll1ll11_opy_, self.bstack1l1lll1l1ll_opy_, test_framework_state)
        TestFramework.bstack1ll11ll1ll1_opy_(ob, {
            TestFramework.bstack1lll1lll1l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll11lllll_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l11ll1l_opy_: [],
            bstack1l11llll1l1_opy_.bstack1ll1111ll1l_opy_: {},
            bstack1l11llll1l1_opy_.bstack1ll11111l11_opy_: {},
            bstack1l11llll1l1_opy_.bstack1ll1l1111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llllll1l11_opy_(ob, TestFramework.bstack1ll1111l11l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llllll1l11_opy_(ob, TestFramework.bstack1llll1lll11_opy_, context.platform_index)
        TestFramework.bstack1lll1lll1ll_opy_[ctx.id] = ob
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᗪ") + str(TestFramework.bstack1lll1lll1ll_opy_.keys()) + bstack11l1l11_opy_ (u"ࠦࠧᗫ"))
        return ob
    def bstack1ll111111ll_opy_(self, instance: bstack1lll1l1ll11_opy_, bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll1111ll11_opy_ = (
            bstack1l11llll1l1_opy_.bstack1ll1l1l111l_opy_
            if bstack1llllll11l1_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else bstack1l11llll1l1_opy_.bstack1ll111ll1ll_opy_
        )
        hook = bstack1l11llll1l1_opy_.bstack1ll111l1l11_opy_(instance, bstack1ll1111ll11_opy_)
        entries = hook.get(TestFramework.bstack1l1lllll11l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l11ll1l_opy_, []))
        return entries
    def bstack1ll11ll1l1l_opy_(self, instance: bstack1lll1l1ll11_opy_, bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_]):
        bstack1ll1111ll11_opy_ = (
            bstack1l11llll1l1_opy_.bstack1ll1l1l111l_opy_
            if bstack1llllll11l1_opy_[1] == bstack1lll11lll1l_opy_.PRE
            else bstack1l11llll1l1_opy_.bstack1ll111ll1ll_opy_
        )
        bstack1l11llll1l1_opy_.bstack1l1llll1l1l_opy_(instance, bstack1ll1111ll11_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l11ll1l_opy_, []).clear()
    def bstack1l1llll1l11_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᗬ")
        global _1ll1l111ll1_opy_
        platform_index = os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᗭ")]
        bstack1ll1111lll1_opy_ = os.path.join(bstack1ll11111l1l_opy_, (bstack1ll11l111l1_opy_ + str(platform_index)), bstack11llll111l1_opy_)
        if not os.path.exists(bstack1ll1111lll1_opy_) or not os.path.isdir(bstack1ll1111lll1_opy_):
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷࡷࠥࡺ࡯ࠡࡲࡵࡳࡨ࡫ࡳࡴࠢࡾࢁࠧᗮ").format(bstack1ll1111lll1_opy_))
            return
        logs = hook.get(bstack11l1l11_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᗯ"), [])
        with os.scandir(bstack1ll1111lll1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l111ll1_opy_:
                    self.logger.info(bstack11l1l11_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢᗰ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l1l11_opy_ (u"ࠥࠦᗱ")
                    log_entry = bstack1ll1l1111l1_opy_(
                        kind=bstack11l1l11_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᗲ"),
                        message=bstack11l1l11_opy_ (u"ࠧࠨᗳ"),
                        level=bstack11l1l11_opy_ (u"ࠨࠢᗴ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1lll1llll_opy_=entry.stat().st_size,
                        bstack1l1lll1lll1_opy_=bstack11l1l11_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᗵ"),
                        bstack1l11l1_opy_=os.path.abspath(entry.path),
                        bstack1ll111lllll_opy_=hook.get(TestFramework.bstack1ll111ll11l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l111ll1_opy_.add(abs_path)
        platform_index = os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᗶ")]
        bstack1ll11l11ll1_opy_ = os.path.join(bstack1ll11111l1l_opy_, (bstack1ll11l111l1_opy_ + str(platform_index)), bstack11llll111l1_opy_, bstack11llll11111_opy_)
        if not os.path.exists(bstack1ll11l11ll1_opy_) or not os.path.isdir(bstack1ll11l11ll1_opy_):
            self.logger.info(bstack11l1l11_opy_ (u"ࠤࡑࡳࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡬࡯ࡶࡰࡧࠤࡦࡺ࠺ࠡࡽࢀࠦᗷ").format(bstack1ll11l11ll1_opy_))
        else:
            self.logger.info(bstack11l1l11_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᗸ").format(bstack1ll11l11ll1_opy_))
            with os.scandir(bstack1ll11l11ll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l111ll1_opy_:
                        self.logger.info(bstack11l1l11_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᗹ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l1l11_opy_ (u"ࠧࠨᗺ")
                        log_entry = bstack1ll1l1111l1_opy_(
                            kind=bstack11l1l11_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᗻ"),
                            message=bstack11l1l11_opy_ (u"ࠢࠣᗼ"),
                            level=bstack11l1l11_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᗽ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1lll1llll_opy_=entry.stat().st_size,
                            bstack1l1lll1lll1_opy_=bstack11l1l11_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᗾ"),
                            bstack1l11l1_opy_=os.path.abspath(entry.path),
                            bstack1ll111lll1l_opy_=hook.get(TestFramework.bstack1ll111ll11l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l111ll1_opy_.add(abs_path)
        hook[bstack11l1l11_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᗿ")] = logs
    def bstack1ll1l111l1l_opy_(
        self,
        bstack1ll11l11l11_opy_: bstack1lll1l1ll11_opy_,
        entries: List[bstack1ll1l1111l1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣᘀ"))
        req.platform_index = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1llll1lll11_opy_)
        req.execution_context.hash = str(bstack1ll11l11l11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l11l11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l11l11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1lll1lll1l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l11l11_opy_, TestFramework.bstack1lll11lllll_opy_)
            log_entry.uuid = entry.bstack1ll111lllll_opy_
            log_entry.test_framework_state = bstack1ll11l11l11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l1l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᘁ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack11l1l11_opy_ (u"ࠨࠢᘂ")
            if entry.kind == bstack11l1l11_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᘃ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1lll1llll_opy_
                log_entry.file_path = entry.bstack1l11l1_opy_
        def bstack1ll11ll1111_opy_():
            bstack1ll1111ll_opy_ = datetime.now()
            try:
                self.bstack1llllllll11_opy_.LogCreatedEvent(req)
                bstack1ll11l11l11_opy_.bstack111lllllll_opy_(bstack11l1l11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᘄ"), datetime.now() - bstack1ll1111ll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1l11_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࢁࡽࠣᘅ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l11ll_opy_.enqueue(bstack1ll11ll1111_opy_)
    def __1ll1l1l1lll_opy_(self, instance) -> None:
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡍࡱࡤࡨࡸࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡪࡧࡴࡦࡵࠣࡥࠥࡪࡩࡤࡶࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡩࡶࡴࡳࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡦࡴࡤࠡࡷࡳࡨࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡵࡷࡥࡹ࡫ࠠࡶࡵ࡬ࡲ࡬ࠦࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᘆ")
        bstack1ll11ll1lll_opy_ = {bstack11l1l11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᘇ"): bstack1ll11llll11_opy_.bstack1ll11llllll_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11ll1ll1_opy_(instance, bstack1ll11ll1lll_opy_)
    @staticmethod
    def bstack1ll111l1l11_opy_(instance: bstack1lll1l1ll11_opy_, bstack1ll1111ll11_opy_: str):
        bstack1ll11l1111l_opy_ = (
            bstack1l11llll1l1_opy_.bstack1ll11111l11_opy_
            if bstack1ll1111ll11_opy_ == bstack1l11llll1l1_opy_.bstack1ll111ll1ll_opy_
            else bstack1l11llll1l1_opy_.bstack1ll1l1111ll_opy_
        )
        bstack1ll1l11l1l1_opy_ = TestFramework.get_state(instance, bstack1ll1111ll11_opy_, None)
        bstack1ll11111lll_opy_ = TestFramework.get_state(instance, bstack1ll11l1111l_opy_, None) if bstack1ll1l11l1l1_opy_ else None
        return (
            bstack1ll11111lll_opy_[bstack1ll1l11l1l1_opy_][-1]
            if isinstance(bstack1ll11111lll_opy_, dict) and len(bstack1ll11111lll_opy_.get(bstack1ll1l11l1l1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l1llll1l1l_opy_(instance: bstack1lll1l1ll11_opy_, bstack1ll1111ll11_opy_: str):
        hook = bstack1l11llll1l1_opy_.bstack1ll111l1l11_opy_(instance, bstack1ll1111ll11_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1lllll11l_opy_, []).clear()
    @staticmethod
    def __1ll111l1ll1_opy_(instance: bstack1lll1l1ll11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥᘈ"), None)):
            return
        if os.getenv(bstack11l1l11_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥᘉ"), bstack11l1l11_opy_ (u"ࠢ࠲ࠤᘊ")) != bstack11l1l11_opy_ (u"ࠣ࠳ࠥᘋ"):
            bstack1l11llll1l1_opy_.logger.warning(bstack11l1l11_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦᘌ"))
            return
        bstack1ll11l11lll_opy_ = {
            bstack11l1l11_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᘍ"): (bstack1l11llll1l1_opy_.bstack1ll1l1l111l_opy_, bstack1l11llll1l1_opy_.bstack1ll1l1111ll_opy_),
            bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᘎ"): (bstack1l11llll1l1_opy_.bstack1ll111ll1ll_opy_, bstack1l11llll1l1_opy_.bstack1ll11111l11_opy_),
        }
        for when in (bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᘏ"), bstack11l1l11_opy_ (u"ࠨࡣࡢ࡮࡯ࠦᘐ"), bstack11l1l11_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᘑ")):
            bstack1l1lllllll1_opy_ = args[1].get_records(when)
            if not bstack1l1lllllll1_opy_:
                continue
            records = [
                bstack1ll1l1111l1_opy_(
                    kind=TestFramework.bstack1l1lllll1ll_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l1l11_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦᘒ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l1l11_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥᘓ")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1lllllll1_opy_
                if isinstance(getattr(r, bstack11l1l11_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᘔ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l1ll1l_opy_, bstack1ll11l1111l_opy_ = bstack1ll11l11lll_opy_.get(when, (None, None))
            bstack1ll11l1l11l_opy_ = TestFramework.get_state(instance, bstack1ll11l1ll1l_opy_, None) if bstack1ll11l1ll1l_opy_ else None
            bstack1ll11111lll_opy_ = TestFramework.get_state(instance, bstack1ll11l1111l_opy_, None) if bstack1ll11l1l11l_opy_ else None
            if isinstance(bstack1ll11111lll_opy_, dict) and len(bstack1ll11111lll_opy_.get(bstack1ll11l1l11l_opy_, [])) > 0:
                hook = bstack1ll11111lll_opy_[bstack1ll11l1l11l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l1lllll11l_opy_ in hook:
                    hook[TestFramework.bstack1l1lllll11l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l11ll1l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l1lllll111_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11llll1l1_opy_.__1ll11ll1l11_opy_(test.location) if hasattr(test, bstack11l1l11_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᘕ")) else getattr(test, bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᘖ"), None)
        test_name = test.name if hasattr(test, bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘗ")) else None
        bstack1ll1l11111l_opy_ = test.fspath.strpath if hasattr(test, bstack11l1l11_opy_ (u"ࠢࡧࡵࡳࡥࡹ࡮ࠢᘘ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll1l11111l_opy_:
            return None
        code = None
        if hasattr(test, bstack11l1l11_opy_ (u"ࠣࡱࡥ࡮ࠧᘙ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11lll1lllll_opy_ = []
        try:
            bstack11lll1lllll_opy_ = bstack1l1l11ll_opy_.bstack1ll1111l_opy_(test)
        except:
            bstack1l11llll1l1_opy_.logger.warning(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸࡪࡹࡴࠡࡵࡦࡳࡵ࡫ࡳ࠭ࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡴࡨࡷࡴࡲࡶࡦࡦࠣ࡭ࡳࠦࡃࡍࡋࠥᘚ"))
        return {
            TestFramework.bstack1llll111ll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1111llll_opy_: test_id,
            TestFramework.bstack1l1llllllll_opy_: test_name,
            TestFramework.bstack1ll111l11l1_opy_: getattr(test, bstack11l1l11_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᘛ"), None),
            TestFramework.bstack1ll1l1l11ll_opy_: bstack1ll1l11111l_opy_,
            TestFramework.bstack1ll111l1l1l_opy_: bstack1l11llll1l1_opy_.__1l1llllll11_opy_(test),
            TestFramework.bstack1ll11lll111_opy_: code,
            TestFramework.bstack1lll11l1l1l_opy_: TestFramework.bstack1ll11ll11l1_opy_,
            TestFramework.bstack1lll111l111_opy_: test_id,
            TestFramework.bstack1l111111l1l_opy_: bstack11lll1lllll_opy_
        }
    @staticmethod
    def __1l1llllll11_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack11l1l11_opy_ (u"ࠦࡴࡽ࡮ࡠ࡯ࡤࡶࡰ࡫ࡲࡴࠤᘜ"), [])
            markers.extend([getattr(m, bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘝ"), None) for m in own_markers if getattr(m, bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘞ"), None)])
            current = getattr(current, bstack11l1l11_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᘟ"), None)
        return markers
    @staticmethod
    def __1ll11ll1l11_opy_(location):
        return bstack11l1l11_opy_ (u"ࠣ࠼࠽ࠦᘠ").join(filter(lambda x: isinstance(x, str), location))