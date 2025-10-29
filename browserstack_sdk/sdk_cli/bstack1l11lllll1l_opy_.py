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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll1llll1_opy_, bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111l1l_opy_ import bstack1lll111l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11l1_opy_, bstack1lll1l1l11l_opy_, bstack1lll1l1llll_opy_, bstack1ll1l1l1l11_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1l11l11_opy_, bstack1ll111lll11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1llll1_opy_ = [bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏟ"), bstack11l11ll_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᏠ"), bstack11l11ll_opy_ (u"ࠢࡤࡱࡱࡪ࡮࡭ࠢᏡ"), bstack11l11ll_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࠤᏢ"), bstack11l11ll_opy_ (u"ࠤࡳࡥࡹ࡮ࠢᏣ")]
bstack1ll11l1l1l1_opy_ = bstack1ll111lll11_opy_()
bstack1ll11111lll_opy_ = bstack11l11ll_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥᏤ")
bstack1l11l11ll1l_opy_ = {
    bstack11l11ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡎࡺࡥ࡮ࠤᏥ"): bstack1l11l1llll1_opy_,
    bstack11l11ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡖࡡࡤ࡭ࡤ࡫ࡪࠨᏦ"): bstack1l11l1llll1_opy_,
    bstack11l11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡍࡰࡦࡸࡰࡪࠨᏧ"): bstack1l11l1llll1_opy_,
    bstack11l11ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡄ࡮ࡤࡷࡸࠨᏨ"): bstack1l11l1llll1_opy_,
    bstack11l11ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡈࡸࡲࡨࡺࡩࡰࡰࠥᏩ"): bstack1l11l1llll1_opy_
    + [
        bstack11l11ll_opy_ (u"ࠤࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࡲࡦࡳࡥࠣᏪ"),
        bstack11l11ll_opy_ (u"ࠥ࡯ࡪࡿࡷࡰࡴࡧࡷࠧᏫ"),
        bstack11l11ll_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩ࡮ࡴࡦࡰࠤᏬ"),
        bstack11l11ll_opy_ (u"ࠧࡱࡥࡺࡹࡲࡶࡩࡹࠢᏭ"),
        bstack11l11ll_opy_ (u"ࠨࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠣᏮ"),
        bstack11l11ll_opy_ (u"ࠢࡤࡣ࡯ࡰࡴࡨࡪࠣᏯ"),
        bstack11l11ll_opy_ (u"ࠣࡵࡷࡥࡷࡺࠢᏰ"),
        bstack11l11ll_opy_ (u"ࠤࡶࡸࡴࡶࠢᏱ"),
        bstack11l11ll_opy_ (u"ࠥࡨࡺࡸࡡࡵ࡫ࡲࡲࠧᏲ"),
        bstack11l11ll_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤᏳ"),
    ],
    bstack11l11ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡪࡰ࠱ࡗࡪࡹࡳࡪࡱࡱࠦᏴ"): [bstack11l11ll_opy_ (u"ࠨࡳࡵࡣࡵࡸࡵࡧࡴࡩࠤᏵ"), bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡸ࡬ࡡࡪ࡮ࡨࡨࠧ᏶"), bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡹࡣࡰ࡮࡯ࡩࡨࡺࡥࡥࠤ᏷"), bstack11l11ll_opy_ (u"ࠤ࡬ࡸࡪࡳࡳࠣᏸ")],
    bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡧࡴࡴࡦࡪࡩ࠱ࡇࡴࡴࡦࡪࡩࠥᏹ"): [bstack11l11ll_opy_ (u"ࠦ࡮ࡴࡶࡰࡥࡤࡸ࡮ࡵ࡮ࡠࡲࡤࡶࡦࡳࡳࠣᏺ"), bstack11l11ll_opy_ (u"ࠧࡧࡲࡨࡵࠥᏻ")],
    bstack11l11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡦࡪࡺࡷࡹࡷ࡫ࡳ࠯ࡈ࡬ࡼࡹࡻࡲࡦࡆࡨࡪࠧᏼ"): [bstack11l11ll_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᏽ"), bstack11l11ll_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤ᏾"), bstack11l11ll_opy_ (u"ࠤࡩࡹࡳࡩࠢ᏿"), bstack11l11ll_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥ᐀"), bstack11l11ll_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨᐁ"), bstack11l11ll_opy_ (u"ࠧ࡯ࡤࡴࠤᐂ")],
    bstack11l11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡦࡪࡺࡷࡹࡷ࡫ࡳ࠯ࡕࡸࡦࡗ࡫ࡱࡶࡧࡶࡸࠧᐃ"): [bstack11l11ll_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧᐄ"), bstack11l11ll_opy_ (u"ࠣࡲࡤࡶࡦࡳࠢᐅ"), bstack11l11ll_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡠ࡫ࡱࡨࡪࡾࠢᐆ")],
    bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡶࡺࡴ࡮ࡦࡴ࠱ࡇࡦࡲ࡬ࡊࡰࡩࡳࠧᐇ"): [bstack11l11ll_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤᐈ"), bstack11l11ll_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࠧᐉ")],
    bstack11l11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴࡭ࡢࡴ࡮࠲ࡸࡺࡲࡶࡥࡷࡹࡷ࡫ࡳ࠯ࡐࡲࡨࡪࡑࡥࡺࡹࡲࡶࡩࡹࠢᐊ"): [bstack11l11ll_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᐋ"), bstack11l11ll_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᐌ")],
    bstack11l11ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥࡷࡱ࠮ࡴࡶࡵࡹࡨࡺࡵࡳࡧࡶ࠲ࡒࡧࡲ࡬ࠤᐍ"): [bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᐎ"), bstack11l11ll_opy_ (u"ࠦࡦࡸࡧࡴࠤᐏ"), bstack11l11ll_opy_ (u"ࠧࡱࡷࡢࡴࡪࡷࠧᐐ")],
}
_1ll1l11l1ll_opy_ = set()
class bstack1l1l1ll1l1l_opy_(bstack1lllll11111_opy_):
    bstack1l11l1l111l_opy_ = bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩ࡫ࡦࡦࡴࡵࡩࡩࠨᐑ")
    bstack1l11l11l11l_opy_ = bstack11l11ll_opy_ (u"ࠢࡊࡐࡉࡓࠧᐒ")
    bstack1l11l1l11l1_opy_ = bstack11l11ll_opy_ (u"ࠣࡇࡕࡖࡔࡘࠢᐓ")
    bstack1l11l1ll11l_opy_: Callable
    bstack1l11l1lll1l_opy_: Callable
    def __init__(self, bstack1l11ll11l1l_opy_, bstack1ll1ll1lll1_opy_):
        super().__init__()
        self.bstack1l111llll11_opy_ = bstack1ll1ll1lll1_opy_
        if os.getenv(bstack11l11ll_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡑ࠴࠵࡞ࠨᐔ"), bstack11l11ll_opy_ (u"ࠥ࠵ࠧᐕ")) != bstack11l11ll_opy_ (u"ࠦ࠶ࠨᐖ") or not self.is_enabled():
            self.logger.warning(bstack11l11ll_opy_ (u"ࠧࠨᐗ") + str(self.__class__.__name__) + bstack11l11ll_opy_ (u"ࠨࠠࡥ࡫ࡶࡥࡧࡲࡥࡥࠤᐘ"))
            return
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.PRE), self.bstack1lll1l1l111_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.POST), self.bstack1lll1ll1lll_opy_)
        for event in bstack1lll1ll11l1_opy_:
            for state in bstack1lll1l1llll_opy_:
                TestFramework.bstack1llllll1l1l_opy_((event, state), self.bstack1l111ll1l11_opy_)
        bstack1l11ll11l1l_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, bstack1llllll11ll_opy_.POST), self.bstack1l11l1l1ll1_opy_)
        self.bstack1l11l1ll11l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l11l111_opy_(bstack1l1l1ll1l1l_opy_.bstack1l11l11l11l_opy_, self.bstack1l11l1ll11l_opy_)
        self.bstack1l11l1lll1l_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l11l111_opy_(bstack1l1l1ll1l1l_opy_.bstack1l11l1l11l1_opy_, self.bstack1l11l1lll1l_opy_)
        self.bstack1l111llll1l_opy_ = builtins.print
        builtins.print = self.bstack1l111ll1ll1_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l111ll1l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l11l_opy_,
        bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll111lll1l_opy_() and instance:
            bstack1l11l111ll1_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llll1ll1l1_opy_
            if test_framework_state == bstack1lll1ll11l1_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1ll11l1_opy_.LOG:
                bstack1lll1l1l11_opy_ = datetime.now()
                entries = f.bstack1ll11lll111_opy_(instance, bstack1llll1ll1l1_opy_)
                if entries:
                    self.bstack1ll11l1ll11_opy_(instance, entries)
                    instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺࠢᐙ"), datetime.now() - bstack1lll1l1l11_opy_)
                    f.bstack1ll11ll11ll_opy_(instance, bstack1llll1ll1l1_opy_)
                instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦᐚ"), datetime.now() - bstack1l11l111ll1_opy_)
                return # do not send this event with the bstack1l111lll1ll_opy_ bstack1l11l1lll11_opy_
            elif (
                test_framework_state == bstack1lll1ll11l1_opy_.TEST
                and test_hook_state == bstack1lll1l1llll_opy_.POST
                and not f.bstack1llllll11l1_opy_(instance, TestFramework.bstack1l1lllll1ll_opy_)
            ):
                self.logger.warning(bstack11l11ll_opy_ (u"ࠤࡧࡶࡴࡶࡰࡪࡰࡪࠤࡩࡻࡥࠡࡶࡲࠤࡱࡧࡣ࡬ࠢࡲࡪࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࠢᐛ") + str(TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1l1lllll1ll_opy_)) + bstack11l11ll_opy_ (u"ࠥࠦᐜ"))
                f.bstack1llll1l1l11_opy_(instance, bstack1l1l1ll1l1l_opy_.bstack1l11l1l111l_opy_, True)
                return # do not send this event bstack1l11l11llll_opy_ bstack1l11l111111_opy_
            elif (
                f.get_state(instance, bstack1l1l1ll1l1l_opy_.bstack1l11l1l111l_opy_, False)
                and test_framework_state == bstack1lll1ll11l1_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1l1llll_opy_.POST
                and f.bstack1llllll11l1_opy_(instance, TestFramework.bstack1l1lllll1ll_opy_)
            ):
                self.logger.warning(bstack11l11ll_opy_ (u"ࠦ࡮ࡴࡪࡦࡥࡷ࡭ࡳ࡭ࠠࡕࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡷࡩ࠳࡚ࡅࡔࡖ࠯ࠤ࡙࡫ࡳࡵࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࡕࡕࡓࡕࠢࠥᐝ") + str(TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1l1lllll1ll_opy_)) + bstack11l11ll_opy_ (u"ࠧࠨᐞ"))
                self.bstack1l111ll1l11_opy_(f, instance, (bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.POST), *args, **kwargs)
            bstack1lll1l1l11_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l111llllll_opy_ = sorted(
                filter(lambda x: x.get(bstack11l11ll_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᐟ"), None), data.pop(bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᐠ"), {}).values()),
                key=lambda x: x[bstack11l11ll_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᐡ")],
            )
            if bstack1lll111l1l1_opy_.bstack1lll1ll1l1l_opy_ in data:
                data.pop(bstack1lll111l1l1_opy_.bstack1lll1ll1l1l_opy_)
            data.update({bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᐢ"): bstack1l111llllll_opy_})
            instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠥ࡮ࡸࡵ࡮࠻ࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᐣ"), datetime.now() - bstack1lll1l1l11_opy_)
            bstack1lll1l1l11_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l1l11ll_opy_)
            instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠦ࡯ࡹ࡯࡯࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᐤ"), datetime.now() - bstack1lll1l1l11_opy_)
            self.bstack1l11l1lll11_opy_(instance, bstack1llll1ll1l1_opy_, event_json=event_json)
            instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡ࡭࡮ࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺࡳࠣᐥ"), datetime.now() - bstack1l11l111ll1_opy_)
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l11l_opy_,
        bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l111l1l1_opy_ import bstack1lllllll1ll_opy_
        bstack1ll11l11lll_opy_ = bstack1lllllll1ll_opy_.bstack1ll11l111ll_opy_(EVENTS.bstack11ll1lll1l_opy_.value)
        self.bstack1l111llll11_opy_.bstack1lll1l11111_opy_(instance, f, bstack1llll1ll1l1_opy_, *args, **kwargs)
        bstack1lllllll1ll_opy_.end(EVENTS.bstack11ll1lll1l_opy_.value, bstack1ll11l11lll_opy_ + bstack11l11ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᐦ"), bstack1ll11l11lll_opy_ + bstack11l11ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᐧ"), status=True, failure=None, test_name=None)
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l11l_opy_,
        bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l111llll11_opy_.bstack1lll1ll11ll_opy_(instance, f, bstack1llll1ll1l1_opy_, *args, **kwargs)
        self.bstack1l111lll111_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1l1l1l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def bstack1l111lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l11l_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡘࡪࡹࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡆࡸࡨࡲࡹࠦࡧࡓࡒࡆࠤࡨࡧ࡬࡭࠼ࠣࡒࡴࠦࡶࡢ࡮࡬ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡤࡢࡶࡤࠦᐨ"))
            return
        bstack1lll1l1l11_opy_ = datetime.now()
        try:
            r = self.bstack1llll1l1ll1_opy_.TestSessionEvent(req)
            instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡪࡼࡥ࡯ࡶࠥᐩ"), datetime.now() - bstack1lll1l1l11_opy_)
            f.bstack1llll1l1l11_opy_(instance, self.bstack1l111llll11_opy_.bstack1lll1lll11l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11l11ll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᐪ") + str(r) + bstack11l11ll_opy_ (u"ࠦࠧᐫ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᐬ") + str(e) + bstack11l11ll_opy_ (u"ࠨࠢᐭ"))
            traceback.print_exc()
            raise e
    def bstack1l11l1l1ll1_opy_(
        self,
        f: bstack1llll1l111l_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        _1l111ll1l1l_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llll1l111l_opy_.bstack1l1ll1ll1ll_opy_(method_name):
            return
        if f.bstack1l1ll1l1lll_opy_(*args) == bstack1llll1l111l_opy_.bstack1l11l1l1l11_opy_:
            bstack1l11l111ll1_opy_ = datetime.now()
            screenshot = result.get(bstack11l11ll_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨᐮ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11l11ll_opy_ (u"ࠣ࡫ࡱࡺࡦࡲࡩࡥࠢࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠦࡩ࡮ࡣࡪࡩࠥࡨࡡࡴࡧ࠹࠸ࠥࡹࡴࡳࠤᐯ"))
                return
            bstack1ll1111ll11_opy_ = self.bstack1l111lllll1_opy_(instance)
            if bstack1ll1111ll11_opy_:
                entry = bstack1ll1l1l1l11_opy_(TestFramework.bstack1l111lll11l_opy_, screenshot)
                self.bstack1ll11l1ll11_opy_(bstack1ll1111ll11_opy_, [entry])
                instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠤࡲ࠵࠶ࡿ࠺ࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡨࡼࡪࡩࡵࡵࡧࠥᐰ"), datetime.now() - bstack1l11l111ll1_opy_)
            else:
                self.logger.warning(bstack11l11ll_opy_ (u"ࠥࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡷࡩࡸࡺࠠࡧࡱࡵࠤࡼ࡮ࡩࡤࡪࠣࡸ࡭࡯ࡳࠡࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠥࡽࡡࡴࠢࡷࡥࡰ࡫࡮ࠡࡤࡼࠤࡩࡸࡩࡷࡧࡵࡁࠥࢁࡽࠣᐱ").format(instance.ref()))
        event = {}
        bstack1ll1111ll11_opy_ = self.bstack1l111lllll1_opy_(instance)
        if bstack1ll1111ll11_opy_:
            self.bstack1l11l1ll111_opy_(event, bstack1ll1111ll11_opy_)
            if event.get(bstack11l11ll_opy_ (u"ࠦࡱࡵࡧࡴࠤᐲ")):
                self.bstack1ll11l1ll11_opy_(bstack1ll1111ll11_opy_, event[bstack11l11ll_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᐳ")])
            else:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡲ࡯ࡨࡵࠣࡪࡴࡸࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡪࡼࡥ࡯ࡶࠥᐴ"))
    @measure(event_name=EVENTS.bstack1l111lll1l1_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def bstack1ll11l1ll11_opy_(
        self,
        bstack1ll1111ll11_opy_: bstack1lll1l1l11l_opy_,
        entries: List[bstack1ll1l1l1l11_opy_],
    ):
        self.bstack1llll11l1l1_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1llll1lll11_opy_)
        req.execution_context.hash = str(bstack1ll1111ll11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1111ll11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1111ll11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1llll11111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1lll11l1ll1_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1lll11l1lll_opy_)
            log_entry.test_framework_state = bstack1ll1111ll11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l11ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᐵ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11l11ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᐶ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l11ll11_opy_
                log_entry.file_path = entry.bstack11lll1_opy_
        def bstack1ll111lllll_opy_():
            bstack1lll1l1l11_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l111lll11l_opy_:
                    bstack1ll1111ll11_opy_.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᐷ"), datetime.now() - bstack1lll1l1l11_opy_)
                elif entry.kind == TestFramework.bstack1l11l11lll1_opy_:
                    bstack1ll1111ll11_opy_.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢᐸ"), datetime.now() - bstack1lll1l1l11_opy_)
                else:
                    bstack1ll1111ll11_opy_.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡱࡵࡧࠣᐹ"), datetime.now() - bstack1lll1l1l11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l11ll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᐺ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l11l1_opy_.enqueue(bstack1ll111lllll_opy_)
    @measure(event_name=EVENTS.bstack1l11l1ll1ll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def bstack1l11l1lll11_opy_(
        self,
        instance: bstack1lll1l1l11l_opy_,
        bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_],
        event_json=None,
    ):
        self.bstack1llll11l1l1_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1lll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11l1ll1_opy_)
        req.test_framework_state = bstack1llll1ll1l1_opy_[0].name
        req.test_hook_state = bstack1llll1ll1l1_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11lll1l1_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll11ll11l1_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l1l11ll_opy_)).encode(bstack11l11ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᐻ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll111lllll_opy_():
            bstack1lll1l1l11_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.TestFrameworkEvent(req)
                instance.bstack11111l1lll_opy_(bstack11l11ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡪࡼࡥ࡯ࡶࠥᐼ"), datetime.now() - bstack1lll1l1l11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l11ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᐽ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l11l1_opy_.enqueue(bstack1ll111lllll_opy_)
    def bstack1l111lllll1_opy_(self, instance: bstack1llll1llll1_opy_):
        bstack1l11l1111ll_opy_ = TestFramework.bstack1l11l1l1111_opy_(instance.context)
        for t in bstack1l11l1111ll_opy_:
            bstack1lll111ll11_opy_ = TestFramework.get_state(t, bstack1lll111l1l1_opy_.bstack1lll1ll1l1l_opy_, [])
            if any(instance is d[1] for d in bstack1lll111ll11_opy_):
                return t
    def bstack1l11l111lll_opy_(self, message):
        self.bstack1l11l1ll11l_opy_(message + bstack11l11ll_opy_ (u"ࠤ࡟ࡲࠧᐾ"))
    def log_error(self, message):
        self.bstack1l11l1lll1l_opy_(message + bstack11l11ll_opy_ (u"ࠥࡠࡳࠨᐿ"))
    def bstack1l11l11l111_opy_(self, level, original_func):
        def bstack1l11l111l11_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11l11ll_opy_ (u"ࠦࡊࡼࡥ࡯ࡶࡇ࡭ࡸࡶࡡࡵࡥ࡫ࡩࡷࡓ࡯ࡥࡷ࡯ࡩࠧᑀ") in message or bstack11l11ll_opy_ (u"ࠧࡡࡓࡅࡍࡆࡐࡎࡣࠢᑁ") in message or bstack11l11ll_opy_ (u"ࠨ࡛ࡘࡧࡥࡈࡷ࡯ࡶࡦࡴࡐࡳࡩࡻ࡬ࡦ࡟ࠥᑂ") in message:
                return return_value
            bstack1l11l1111ll_opy_ = TestFramework.bstack1l111ll1lll_opy_()
            if not bstack1l11l1111ll_opy_:
                return return_value
            bstack1ll1111ll11_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l1111ll_opy_
                    if TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1lll11l1lll_opy_)
                ),
                None,
            )
            if not bstack1ll1111ll11_opy_:
                return return_value
            entry = bstack1ll1l1l1l11_opy_(TestFramework.bstack1ll111l1111_opy_, message, level)
            self.bstack1ll11l1ll11_opy_(bstack1ll1111ll11_opy_, [entry])
            return return_value
        return bstack1l11l111l11_opy_
    def bstack1l111ll1ll1_opy_(self):
        def bstack1l11l1ll1l1_opy_(*args, **kwargs):
            try:
                self.bstack1l111llll1l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11l11ll_opy_ (u"ࠧࠡࠩᑃ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11l11ll_opy_ (u"ࠣࡇࡹࡩࡳࡺࡄࡪࡵࡳࡥࡹࡩࡨࡦࡴࡐࡳࡩࡻ࡬ࡦࠤᑄ") in message:
                    return
                bstack1l11l1111ll_opy_ = TestFramework.bstack1l111ll1lll_opy_()
                if not bstack1l11l1111ll_opy_:
                    return
                bstack1ll1111ll11_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l1111ll_opy_
                        if TestFramework.bstack1llllll11l1_opy_(instance, TestFramework.bstack1lll11l1lll_opy_)
                    ),
                    None,
                )
                if not bstack1ll1111ll11_opy_:
                    return
                entry = bstack1ll1l1l1l11_opy_(TestFramework.bstack1ll111l1111_opy_, message, bstack1l1l1ll1l1l_opy_.bstack1l11l11l11l_opy_)
                self.bstack1ll11l1ll11_opy_(bstack1ll1111ll11_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l111llll1l_opy_(bstack11ll111l_opy_ (u"ࠤ࡞ࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࡡࠥࡒ࡯ࡨࠢࡦࡥࡵࡺࡵࡳࡧࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࡪࢃࠢᑅ"))
                except:
                    pass
        return bstack1l11l1ll1l1_opy_
    def bstack1l11l1ll111_opy_(self, event: dict, instance=None) -> None:
        global _1ll1l11l1ll_opy_
        levels = [bstack11l11ll_opy_ (u"ࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨᑆ"), bstack11l11ll_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᑇ")]
        bstack1l111ll11l1_opy_ = bstack11l11ll_opy_ (u"ࠧࠨᑈ")
        if instance is not None:
            try:
                bstack1l111ll11l1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll11l1lll_opy_)
            except Exception as e:
                self.logger.warning(bstack11l11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡵࡶ࡫ࡧࠤ࡫ࡸ࡯࡮ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠦᑉ").format(e))
        bstack1l11l111l1l_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᑊ")]
                bstack1ll1l111111_opy_ = os.path.join(bstack1ll11l1l1l1_opy_, (bstack1ll11111lll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1l111111_opy_):
                    self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡳࡵࡴࠡࡲࡵࡩࡸ࡫࡮ࡵࠢࡩࡳࡷࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡘࡪࡹࡴࠡࡣࡱࡨࠥࡈࡵࡪ࡮ࡧࠤࡱ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡽࢀࠦᑋ").format(bstack1ll1l111111_opy_))
                    continue
                file_names = os.listdir(bstack1ll1l111111_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1l111111_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1l11l1ll_opy_:
                        self.logger.info(bstack11l11ll_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢᑌ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l11l1ll_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l11l1ll_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11l11ll_opy_ (u"ࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨᑍ"):
                                entry = bstack1ll1l1l1l11_opy_(
                                    kind=bstack11l11ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᑎ"),
                                    message=bstack11l11ll_opy_ (u"ࠧࠨᑏ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l11ll11_opy_=file_size,
                                    bstack1ll1l11l1l1_opy_=bstack11l11ll_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᑐ"),
                                    bstack11lll1_opy_=os.path.abspath(file_path),
                                    bstack1l1ll11l1l_opy_=bstack1l111ll11l1_opy_
                                )
                            elif level == bstack11l11ll_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᑑ"):
                                entry = bstack1ll1l1l1l11_opy_(
                                    kind=bstack11l11ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᑒ"),
                                    message=bstack11l11ll_opy_ (u"ࠤࠥᑓ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l11ll11_opy_=file_size,
                                    bstack1ll1l11l1l1_opy_=bstack11l11ll_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᑔ"),
                                    bstack11lll1_opy_=os.path.abspath(file_path),
                                    bstack1ll1111lll1_opy_=bstack1l111ll11l1_opy_
                                )
                            bstack1l11l111l1l_opy_.append(entry)
                            _1ll1l11l1ll_opy_.add(abs_path)
                        except Exception as bstack1l111ll11ll_opy_:
                            self.logger.error(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡳࡣ࡬ࡷࡪࡪࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᑕ").format(bstack1l111ll11ll_opy_))
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡴࡤ࡭ࡸ࡫ࡤࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡽࢀࠦᑖ").format(e))
        event[bstack11l11ll_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᑗ")] = bstack1l11l111l1l_opy_
class bstack1l11l1l11ll_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l11ll11_opy_ = set()
        kwargs[bstack11l11ll_opy_ (u"ࠢࡴ࡭࡬ࡴࡰ࡫ࡹࡴࠤᑘ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l1111l1_opy_(obj, self.bstack1l11l11ll11_opy_)
def bstack1l11l1l1lll_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l1111l1_opy_(obj, bstack1l11l11ll11_opy_=None, max_depth=3):
    if bstack1l11l11ll11_opy_ is None:
        bstack1l11l11ll11_opy_ = set()
    if id(obj) in bstack1l11l11ll11_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l11ll11_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l11l1l1_opy_ = TestFramework.bstack1ll11l11l11_opy_(obj)
    bstack1l11l11111l_opy_ = next((k.lower() in bstack1l11l11l1l1_opy_.lower() for k in bstack1l11l11ll1l_opy_.keys()), None)
    if bstack1l11l11111l_opy_:
        obj = TestFramework.bstack1ll11111111_opy_(obj, bstack1l11l11ll1l_opy_[bstack1l11l11111l_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11l11ll_opy_ (u"ࠣࡡࡢࡷࡱࡵࡴࡴࡡࡢࠦᑙ")):
            keys = getattr(obj, bstack11l11ll_opy_ (u"ࠤࡢࡣࡸࡲ࡯ࡵࡵࡢࡣࠧᑚ"), [])
        elif hasattr(obj, bstack11l11ll_opy_ (u"ࠥࡣࡤࡪࡩࡤࡶࡢࡣࠧᑛ")):
            keys = getattr(obj, bstack11l11ll_opy_ (u"ࠦࡤࡥࡤࡪࡥࡷࡣࡤࠨᑜ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11l11ll_opy_ (u"ࠧࡥࠢᑝ"))}
        if not obj and bstack1l11l11l1l1_opy_ == bstack11l11ll_opy_ (u"ࠨࡰࡢࡶ࡫ࡰ࡮ࡨ࠮ࡑࡱࡶ࡭ࡽࡖࡡࡵࡪࠥᑞ"):
            obj = {bstack11l11ll_opy_ (u"ࠢࡱࡣࡷ࡬ࠧᑟ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l1l1lll_opy_(key) or str(key).startswith(bstack11l11ll_opy_ (u"ࠣࡡࠥᑠ")):
            continue
        if value is not None and bstack1l11l1l1lll_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l1111l1_opy_(value, bstack1l11l11ll11_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l1111l1_opy_(o, bstack1l11l11ll11_opy_, max_depth) for o in value]))
    return result or None