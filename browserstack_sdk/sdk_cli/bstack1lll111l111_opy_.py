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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lll111lll1_opy_,
    bstack1lllllll11l_opy_,
    bstack1lll1l1lll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_, bstack1llll111111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1llll_opy_ import bstack1lll1llllll_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11l1lll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11l1111_opy_(bstack1lll1llllll_opy_):
    bstack1lll1l1ll1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡷ࡯ࡶࡦࡴࡶࠦᅷ")
    bstack1lll11ll1l1_opy_ = bstack1lll11l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅸ")
    bstack1lll1l11l1l_opy_ = bstack1lll11l_opy_ (u"ࠢ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᅹ")
    bstack1lll11lll1l_opy_ = bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅺ")
    bstack1lll11ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡠࡴࡨࡪࡸࠨᅻ")
    bstack1lll11l1ll1_opy_ = bstack1lll11l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡥࡵࡩࡦࡺࡥࡥࠤᅼ")
    bstack1lll1l1l1ll_opy_ = bstack1lll11l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢᅽ")
    bstack1lll1ll1ll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡷࡹࡧࡴࡶࡵࠥᅾ")
    def __init__(self):
        super().__init__(bstack1lll1ll1111_opy_=self.bstack1lll1l1ll1l_opy_, frameworks=[bstack1llllll1ll1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.BEFORE_EACH, bstack1lll11lll11_opy_.POST), self.bstack1lll11l11l1_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll111l1l1_opy_ = self.bstack1lll11l111l_opy_(instance.context)
        if not bstack1lll111l1l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅿ") + str(bstack1lllll1l111_opy_) + bstack1lll11l_opy_ (u"ࠢࠣᆀ"))
        f.bstack1llll1ll11l_opy_(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, bstack1lll111l1l1_opy_)
        bstack1lll11111l1_opy_ = self.bstack1lll11l111l_opy_(instance.context, bstack1lll1111l1l_opy_=False)
        f.bstack1llll1ll11l_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1l11l1l_opy_, bstack1lll11111l1_opy_)
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11l1_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1l1ll_opy_, False):
            self.__1lll111111l_opy_(f,instance,bstack1lllll1l111_opy_)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11l1_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1l1ll_opy_, False):
            self.__1lll111111l_opy_(f, instance, bstack1lllll1l111_opy_)
        if not f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1ll1ll1_opy_, False):
            self.__1lll1111111_opy_(f, instance, bstack1lllll1l111_opy_)
    def bstack1lll111l11l_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll1111ll1_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1ll1ll1_opy_, False):
            return
        driver.execute_script(
            bstack1lll11l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆁ").format(
                json.dumps(
                    {
                        bstack1lll11l_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆂ"): bstack1lll11l_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᆃ"),
                        bstack1lll11l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆄ"): {bstack1lll11l_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᆅ"): result},
                    }
                )
            )
        )
        f.bstack1llll1ll11l_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1ll1ll1_opy_, True)
    def bstack1lll11l111l_opy_(self, context: bstack1lll1l1lll1_opy_, bstack1lll1111l1l_opy_= True):
        if bstack1lll1111l1l_opy_:
            bstack1lll111l1l1_opy_ = self.bstack1lll1ll1lll_opy_(context, reverse=True)
        else:
            bstack1lll111l1l1_opy_ = self.bstack1lll1ll11ll_opy_(context, reverse=True)
        return [f for f in bstack1lll111l1l1_opy_ if f[1].state != bstack1111111111_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l111llll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1lll1111111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᆆ")).get(bstack1lll11l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᆇ")):
            bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
            if not bstack1lll111l1l1_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᆈ") + str(bstack1lllll1l111_opy_) + bstack1lll11l_opy_ (u"ࠤࠥᆉ"))
                return
            driver = bstack1lll111l1l1_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1lll11l_opy_, None)
            if not status:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᆊ") + str(bstack1lllll1l111_opy_) + bstack1lll11l_opy_ (u"ࠦࠧᆋ"))
                return
            bstack1lll1l1ll11_opy_ = {bstack1lll11l_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᆌ"): status.lower()}
            bstack1lll1lll1l1_opy_ = f.get_state(instance, TestFramework.bstack1lll11lllll_opy_, None)
            if status.lower() == bstack1lll11l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᆍ") and bstack1lll1lll1l1_opy_ is not None:
                bstack1lll1l1ll11_opy_[bstack1lll11l_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᆎ")] = bstack1lll1lll1l1_opy_[0][bstack1lll11l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᆏ")][0] if isinstance(bstack1lll1lll1l1_opy_, list) else str(bstack1lll1lll1l1_opy_)
            driver.execute_script(
                bstack1lll11l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆐ").format(
                    json.dumps(
                        {
                            bstack1lll11l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆑ"): bstack1lll11l_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᆒ"),
                            bstack1lll11l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆓ"): bstack1lll1l1ll11_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1ll11l_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1ll1ll1_opy_, True)
    @measure(event_name=EVENTS.bstack11lllll111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def __1lll111111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᆔ")).get(bstack1lll11l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᆕ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll1111lll_opy_, None)
            if not test_name:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᆖ"))
                return
            bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
            if not bstack1lll111l1l1_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᆗ") + str(bstack1lllll1l111_opy_) + bstack1lll11l_opy_ (u"ࠥࠦᆘ"))
                return
            for bstack1lll111l1ll_opy_, bstack1lll1111l11_opy_ in bstack1lll111l1l1_opy_:
                if not bstack1llllll1ll1_opy_.bstack1lll1111ll1_opy_(bstack1lll1111l11_opy_):
                    continue
                driver = bstack1lll111l1ll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1lll11l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᆙ").format(
                        json.dumps(
                            {
                                bstack1lll11l_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᆚ"): bstack1lll11l_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᆛ"),
                                bstack1lll11l_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆜ"): {bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨᆝ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1ll11l_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1l1l1ll_opy_, True)
    def bstack1llll11l111_opy_(
        self,
        instance: bstack1llll111111_opy_,
        f: TestFramework,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11l1_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        bstack1lll111l1l1_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])]
        if not bstack1lll111l1l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤᆞ"))
            return
        if not bstack1lll11l1lll_opy_():
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᆟ"))
            return
        for bstack1lll111ll11_opy_ in bstack1lll111l1l1_opy_:
            driver = bstack1lll111ll11_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1lll11l_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤᆠ") + str(timestamp)
            driver.execute_script(
                bstack1lll11l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆡ").format(
                    json.dumps(
                        {
                            bstack1lll11l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆢ"): bstack1lll11l_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤᆣ"),
                            bstack1lll11l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆤ"): {
                                bstack1lll11l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᆥ"): bstack1lll11l_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢᆦ"),
                                bstack1lll11l_opy_ (u"ࠦࡩࡧࡴࡢࠤᆧ"): data,
                                bstack1lll11l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦᆨ"): bstack1lll11l_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧᆩ")
                            }
                        }
                    )
                )
            )
    def bstack1lll11ll111_opy_(
        self,
        instance: bstack1llll111111_opy_,
        f: TestFramework,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l11l1_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        keys = [
            bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_,
            bstack1lll11l1111_opy_.bstack1lll1l11l1l_opy_,
        ]
        bstack1lll111l1l1_opy_ = []
        for key in keys:
            bstack1lll111l1l1_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll111l1l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡲࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤᆪ"))
            return
        if f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11l1ll1_opy_, False):
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡆࡆ࡙ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡤࡴࡨࡥࡹ࡫ࡤࠣᆫ"))
            return
        self.bstack1llllll1lll_opy_()
        bstack11ll11l1l_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l111_opy_)
        req.test_framework_state = bstack1lllll1l111_opy_[0].name
        req.test_hook_state = bstack1lllll1l111_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11ll11l_opy_)
        for bstack1lll111l1ll_opy_, driver in bstack1lll111l1l1_opy_:
            try:
                webdriver = bstack1lll111l1ll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠤ࡚ࡩࡧࡊࡲࡪࡸࡨࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠡࠪࡵࡩ࡫࡫ࡲࡦࡰࡦࡩࠥ࡫ࡸࡱ࡫ࡵࡩࡩ࠯ࠢᆬ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1lll11l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠤᆭ")
                    if bstack1llllll1ll1_opy_.get_state(driver, bstack1llllll1ll1_opy_.bstack1lll11111ll_opy_, False)
                    else bstack1lll11l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠥᆮ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llllll1ll1_opy_.get_state(driver, bstack1llllll1ll1_opy_.bstack1llll111lll_opy_, bstack1lll11l_opy_ (u"ࠧࠨᆯ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llllll1ll1_opy_.get_state(driver, bstack1llllll1ll1_opy_.bstack1llll111l1l_opy_, bstack1lll11l_opy_ (u"ࠨࠢᆰ"))
                caps = None
                if hasattr(webdriver, bstack1lll11l_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᆱ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡧ࡭ࡷ࡫ࡣࡵ࡮ࡼࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᆲ"))
                    except Exception as e:
                        self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠦࠢᆳ") + str(e) + bstack1lll11l_opy_ (u"ࠥࠦᆴ"))
                try:
                    bstack1lll111llll_opy_ = json.dumps(caps).encode(bstack1lll11l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᆵ")) if caps else bstack1lll111ll1l_opy_ (u"ࠧࢁࡽࠣᆶ")
                    req.capabilities = bstack1lll111llll_opy_
                except Exception as e:
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡧࡦࡶࡢࡧࡧࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡵࡨࡶ࡮ࡧ࡬ࡪࡼࡨࠤࡨࡧࡰࡴࠢࡩࡳࡷࠦࡲࡦࡳࡸࡩࡸࡺ࠺ࠡࠤᆷ") + str(e) + bstack1lll11l_opy_ (u"ࠢࠣᆸ"))
            except Exception as e:
                self.logger.error(bstack1lll11l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡺࡥ࡮࠼ࠣࠦᆹ") + str(str(e)) + bstack1lll11l_opy_ (u"ࠤࠥᆺ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll11l1lll_opy_() and len(bstack1lll111l1l1_opy_) == 0:
            bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll111l1l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆻ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠦࠧᆼ"))
            return {}
        if len(bstack1lll111l1l1_opy_) > 1:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆽ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠨࠢᆾ"))
            return {}
        bstack1lll111l1ll_opy_, bstack1lll11llll1_opy_ = bstack1lll111l1l1_opy_[0]
        driver = bstack1lll111l1ll_opy_()
        if not driver:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆿ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠣࠤᇀ"))
            return {}
        capabilities = f.get_state(bstack1lll11llll1_opy_, bstack1llllll1ll1_opy_.bstack1lll1llll1l_opy_)
        if not capabilities:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇁ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠥࠦᇂ"))
            return {}
        return capabilities.get(bstack1lll11l_opy_ (u"ࠦࡦࡲࡷࡢࡻࡶࡑࡦࡺࡣࡩࠤᇃ"), {})
    def bstack1lll1l11111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll11l1lll_opy_() and len(bstack1lll111l1l1_opy_) == 0:
            bstack1lll111l1l1_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll111l1l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇄ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠨࠢᇅ"))
            return
        if len(bstack1lll111l1l1_opy_) > 1:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇆ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠣࠤᇇ"))
        bstack1lll111l1ll_opy_, bstack1lll11llll1_opy_ = bstack1lll111l1l1_opy_[0]
        driver = bstack1lll111l1ll_opy_()
        if not driver:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇈ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠥࠦᇉ"))
            return
        return driver