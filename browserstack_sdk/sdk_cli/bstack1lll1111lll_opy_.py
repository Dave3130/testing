# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import (
    bstack1llll11llll_opy_,
    bstack1llll11l1l1_opy_,
    bstack1lll1111l1l_opy_,
    bstack1llll1l1l11_opy_,
    bstack1lll1l1l1ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llll11ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_, bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll1111l1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11ll1ll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11111l1_opy_(bstack1llll1111l1_opy_):
    bstack1lll1llll11_opy_ = bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡸࡩࡷࡧࡵࡷࠧᆍ")
    bstack1lll11lllll_opy_ = bstack11ll1l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᆎ")
    bstack1lll1ll111l_opy_ = bstack11ll1l_opy_ (u"ࠣࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᆏ")
    bstack1lll1ll11ll_opy_ = bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᆐ")
    bstack1lll1l111l1_opy_ = bstack11ll1l_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡡࡵࡩ࡫ࡹࠢᆑ")
    bstack1lll1ll1l11_opy_ = bstack11ll1l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥᆒ")
    bstack1lll1lll11l_opy_ = bstack11ll1l_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣᆓ")
    bstack1lll1l1llll_opy_ = bstack11ll1l_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡸࡺࡡࡵࡷࡶࠦᆔ")
    def __init__(self):
        super().__init__(bstack1lll11lll11_opy_=self.bstack1lll1llll11_opy_, frameworks=[bstack1llll11ll11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.BEFORE_EACH, bstack1lll11lll1l_opy_.POST), self.bstack1lll1111ll1_opy_)
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1lll1llll1l_opy_)
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1l11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1111ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll111l1ll_opy_ = self.bstack1lll111lll1_opy_(instance.context)
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᆕ") + str(bstack1lllllllll1_opy_) + bstack11ll1l_opy_ (u"ࠣࠤᆖ"))
        f.bstack1llll1l1lll_opy_(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, bstack1lll111l1ll_opy_)
        bstack1lll1111111_opy_ = self.bstack1lll111lll1_opy_(instance.context, bstack1lll111l1l1_opy_=False)
        f.bstack1llll1l1lll_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1ll111l_opy_, bstack1lll1111111_opy_)
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111ll1_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1lll11l_opy_, False):
            self.__1lll111ll1l_opy_(f,instance,bstack1lllllllll1_opy_)
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111ll1_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1lll11l_opy_, False):
            self.__1lll111ll1l_opy_(f, instance, bstack1lllllllll1_opy_)
        if not f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, False):
            self.__1lll111l111_opy_(f, instance, bstack1lllllllll1_opy_)
    def bstack1lll1111l11_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll111l11l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, False):
            return
        driver.execute_script(
            bstack11ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆗ").format(
                json.dumps(
                    {
                        bstack11ll1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆘ"): bstack11ll1l_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᆙ"),
                        bstack11ll1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆚ"): {bstack11ll1l_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᆛ"): result},
                    }
                )
            )
        )
        f.bstack1llll1l1lll_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, True)
    def bstack1lll111lll1_opy_(self, context: bstack1lll1l1l1ll_opy_, bstack1lll111l1l1_opy_= True):
        if bstack1lll111l1l1_opy_:
            bstack1lll111l1ll_opy_ = self.bstack1llll1111ll_opy_(context, reverse=True)
        else:
            bstack1lll111l1ll_opy_ = self.bstack1lll1l11l1l_opy_(context, reverse=True)
        return [f for f in bstack1lll111l1ll_opy_ if f[1].state != bstack1llll11llll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1ll1ll111l_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def __1lll111l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧᆜ")).get(bstack11ll1l_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᆝ")):
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])
            if not bstack1lll111l1ll_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᆞ") + str(bstack1lllllllll1_opy_) + bstack11ll1l_opy_ (u"ࠥࠦᆟ"))
                return
            driver = bstack1lll111l1ll_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1l11111_opy_, None)
            if not status:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᆠ") + str(bstack1lllllllll1_opy_) + bstack11ll1l_opy_ (u"ࠧࠨᆡ"))
                return
            bstack1lll1ll1ll1_opy_ = {bstack11ll1l_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᆢ"): status.lower()}
            bstack1lll1ll1111_opy_ = f.get_state(instance, TestFramework.bstack1lll1l11l11_opy_, None)
            if status.lower() == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᆣ") and bstack1lll1ll1111_opy_ is not None:
                bstack1lll1ll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᆤ")] = bstack1lll1ll1111_opy_[0][bstack11ll1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᆥ")][0] if isinstance(bstack1lll1ll1111_opy_, list) else str(bstack1lll1ll1111_opy_)
            driver.execute_script(
                bstack11ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᆦ").format(
                    json.dumps(
                        {
                            bstack11ll1l_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᆧ"): bstack11ll1l_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᆨ"),
                            bstack11ll1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆩ"): bstack1lll1ll1ll1_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1l1lll_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, True)
    @measure(event_name=EVENTS.bstack1llll1l111_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def __1lll111ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧᆪ")).get(bstack11ll1l_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᆫ")):
            test_name = f.get_state(instance, TestFramework.bstack1ll1llllll1_opy_, None)
            if not test_name:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᆬ"))
                return
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])
            if not bstack1lll111l1ll_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᆭ") + str(bstack1lllllllll1_opy_) + bstack11ll1l_opy_ (u"ࠦࠧᆮ"))
                return
            for bstack1ll1lllll1l_opy_, bstack1lll11111ll_opy_ in bstack1lll111l1ll_opy_:
                if not bstack1llll11ll11_opy_.bstack1lll111l11l_opy_(bstack1lll11111ll_opy_):
                    continue
                driver = bstack1ll1lllll1l_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆯ").format(
                        json.dumps(
                            {
                                bstack11ll1l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆰ"): bstack11ll1l_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᆱ"),
                                bstack11ll1l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆲ"): {bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆳ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1l1lll_opy_(instance, bstack1lll11111l1_opy_.bstack1lll1lll11l_opy_, True)
    def bstack1lll1l111ll_opy_(
        self,
        instance: bstack1lll1l11lll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111ll1_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        bstack1lll111l1ll_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])]
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢࡷࡳࠥࡲࡩ࡯࡭ࠥᆴ"))
            return
        if not bstack1lll11ll1ll_opy_():
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᆵ"))
            return
        for bstack1lll111ll11_opy_ in bstack1lll111l1ll_opy_:
            driver = bstack1lll111ll11_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11ll1l_opy_ (u"ࠧࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡘࡿ࡮ࡤ࠼ࠥᆶ") + str(timestamp)
            driver.execute_script(
                bstack11ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᆷ").format(
                    json.dumps(
                        {
                            bstack11ll1l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᆸ"): bstack11ll1l_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥᆹ"),
                            bstack11ll1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᆺ"): {
                                bstack11ll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣᆻ"): bstack11ll1l_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣᆼ"),
                                bstack11ll1l_opy_ (u"ࠧࡪࡡࡵࡣࠥᆽ"): data,
                                bstack11ll1l_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧᆾ"): bstack11ll1l_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨᆿ")
                            }
                        }
                    )
                )
            )
    def bstack1llll111111_opy_(
        self,
        instance: bstack1lll1l11lll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111ll1_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        keys = [
            bstack1lll11111l1_opy_.bstack1lll11lllll_opy_,
            bstack1lll11111l1_opy_.bstack1lll1ll111l_opy_,
        ]
        bstack1lll111l1ll_opy_ = []
        for key in keys:
            bstack1lll111l1ll_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡳࡿࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢࡷࡳࠥࡲࡩ࡯࡭ࠥᇀ"))
            return
        if f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1ll1l11_opy_, False):
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡇࡇ࡚ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡥࡵࡩࡦࡺࡥࡥࠤᇁ"))
            return
        self.bstack1llll1l11l1_opy_()
        bstack1ll11ll111_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1llll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1lll1_opy_)
        req.test_framework_state = bstack1lllllllll1_opy_[0].name
        req.test_hook_state = bstack1lllllllll1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        for bstack1ll1lllll1l_opy_, driver in bstack1lll111l1ll_opy_:
            try:
                webdriver = bstack1ll1lllll1l_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11ll1l_opy_ (u"࡛ࠥࡪࡨࡄࡳ࡫ࡹࡩࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡ࡫ࡶࠤࡓࡵ࡮ࡦࠢࠫࡶࡪ࡬ࡥࡳࡧࡱࡧࡪࠦࡥࡹࡲ࡬ࡶࡪࡪࠩࠣᇂ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11ll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥᇃ")
                    if bstack1llll11ll11_opy_.get_state(driver, bstack1llll11ll11_opy_.bstack1lll111llll_opy_, False)
                    else bstack11ll1l_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠦᇄ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llll11ll11_opy_.get_state(driver, bstack1llll11ll11_opy_.bstack1lll11l1lll_opy_, bstack11ll1l_opy_ (u"ࠨࠢᇅ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llll11ll11_opy_.get_state(driver, bstack1llll11ll11_opy_.bstack1lll1ll1l1l_opy_, bstack11ll1l_opy_ (u"ࠢࠣᇆ"))
                caps = None
                if hasattr(webdriver, bstack11ll1l_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᇇ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡨ࡮ࡸࡥࡤࡶ࡯ࡽࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᇈ"))
                    except Exception as e:
                        self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡶࡴࡳࠠࡥࡴ࡬ࡺࡪࡸ࠮ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡀࠠࠣᇉ") + str(e) + bstack11ll1l_opy_ (u"ࠦࠧᇊ"))
                try:
                    bstack1ll1lllllll_opy_ = json.dumps(caps).encode(bstack11ll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇋ")) if caps else bstack1lll111111l_opy_ (u"ࠨࡻࡾࠤᇌ")
                    req.capabilities = bstack1ll1lllllll_opy_
                except Exception as e:
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡨࡧࡷࡣࡨࡨࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢࡶࡩࡷ࡯ࡡ࡭࡫ࡽࡩࠥࡩࡡࡱࡵࠣࡪࡴࡸࠠࡳࡧࡴࡹࡪࡹࡴ࠻ࠢࠥᇍ") + str(e) + bstack11ll1l_opy_ (u"ࠣࠤᇎ"))
            except Exception as e:
                self.logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡪࡲࡪࡸࡨࡶࠥ࡯ࡴࡦ࡯࠽ࠤࠧᇏ") + str(str(e)) + bstack11ll1l_opy_ (u"ࠥࠦᇐ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll11l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll11ll1ll_opy_() and len(bstack1lll111l1ll_opy_) == 0:
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1ll111l_opy_, [])
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇑ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠧࠨᇒ"))
            return {}
        if len(bstack1lll111l1ll_opy_) > 1:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇓ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣᇔ"))
            return {}
        bstack1ll1lllll1l_opy_, bstack1llll11111l_opy_ = bstack1lll111l1ll_opy_[0]
        driver = bstack1ll1lllll1l_opy_()
        if not driver:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇕ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠤࠥᇖ"))
            return {}
        capabilities = f.get_state(bstack1llll11111l_opy_, bstack1llll11ll11_opy_.bstack1lll1l1111l_opy_)
        if not capabilities:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇗ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧᇘ"))
            return {}
        return capabilities.get(bstack11ll1l_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥᇙ"), {})
    def bstack1lll1lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll11ll1ll_opy_() and len(bstack1lll111l1ll_opy_) == 0:
            bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll1ll111l_opy_, [])
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇚ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣᇛ"))
            return
        if len(bstack1lll111l1ll_opy_) > 1:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇜ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠤࠥᇝ"))
        bstack1ll1lllll1l_opy_, bstack1llll11111l_opy_ = bstack1lll111l1ll_opy_[0]
        driver = bstack1ll1lllll1l_opy_()
        if not driver:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇞ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧᇟ"))
            return
        return driver