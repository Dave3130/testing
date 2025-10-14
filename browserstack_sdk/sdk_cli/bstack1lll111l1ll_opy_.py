# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import (
    bstack1llll1l1lll_opy_,
    bstack1111111l1l_opy_,
    bstack1lll11ll111_opy_,
    bstack1111111111_opy_,
    bstack1lll1ll111l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1llllll11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_, bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1l111l1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1llll11llll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111lll1_opy_(bstack1lll1l111l1_opy_):
    bstack1llll111l1l_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨᅖ")
    bstack1llll11l11l_opy_ = bstack11l1l11_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᅗ")
    bstack1lll1llllll_opy_ = bstack11l1l11_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅘ")
    bstack1lll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᅙ")
    bstack1llll11111l_opy_ = bstack11l1l11_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣᅚ")
    bstack1llll111111_opy_ = bstack11l1l11_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᅛ")
    bstack1llll11lll1_opy_ = bstack11l1l11_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᅜ")
    bstack1lll1l1l1ll_opy_ = bstack11l1l11_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧᅝ")
    def __init__(self):
        super().__init__(bstack1llll1l111l_opy_=self.bstack1llll111l1l_opy_, frameworks=[bstack1llllll11l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.BEFORE_EACH, bstack1llll1111l1_opy_.POST), self.bstack1lll11ll1ll_opy_)
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.PRE), self.bstack1lll1llll1l_opy_)
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11ll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll111ll1l_opy_ = self.bstack1lll11l1ll1_opy_(instance.context)
        if not bstack1lll111ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᅞ") + str(bstack11111111l1_opy_) + bstack11l1l11_opy_ (u"ࠤࠥᅟ"))
        f.bstack1llll1l1l1l_opy_(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, bstack1lll111ll1l_opy_)
        bstack1lll11l111l_opy_ = self.bstack1lll11l1ll1_opy_(instance.context, bstack1lll11ll11l_opy_=False)
        f.bstack1llll1l1l1l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1llllll_opy_, bstack1lll11l111l_opy_)
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll1ll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11lll1_opy_, False):
            self.__1lll11l11l1_opy_(f,instance,bstack11111111l1_opy_)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll1ll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11lll1_opy_, False):
            self.__1lll11l11l1_opy_(f, instance, bstack11111111l1_opy_)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l1l1ll_opy_, False):
            self.__1lll11l1111_opy_(f, instance, bstack11111111l1_opy_)
    def bstack1lll11lll1l_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11l1lll_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l1l1ll_opy_, False):
            return
        driver.execute_script(
            bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᅠ").format(
                json.dumps(
                    {
                        bstack11l1l11_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᅡ"): bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᅢ"),
                        bstack11l1l11_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᅣ"): {bstack11l1l11_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᅤ"): result},
                    }
                )
            )
        )
        f.bstack1llll1l1l1l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1l1l1ll_opy_, True)
    def bstack1lll11l1ll1_opy_(self, context: bstack1lll1ll111l_opy_, bstack1lll11ll11l_opy_= True):
        if bstack1lll11ll11l_opy_:
            bstack1lll111ll1l_opy_ = self.bstack1lll1ll1111_opy_(context, reverse=True)
        else:
            bstack1lll111ll1l_opy_ = self.bstack1lll1l111ll_opy_(context, reverse=True)
        return [f for f in bstack1lll111ll1l_opy_ if f[1].state != bstack1llll1l1lll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1lll11l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᅥ")).get(bstack11l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᅦ")):
            bstack1lll111ll1l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, [])
            if not bstack1lll111ll1l_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᅧ") + str(bstack11111111l1_opy_) + bstack11l1l11_opy_ (u"ࠦࠧᅨ"))
                return
            driver = bstack1lll111ll1l_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1llll111ll1_opy_, None)
            if not status:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅩ") + str(bstack11111111l1_opy_) + bstack11l1l11_opy_ (u"ࠨࠢᅪ"))
                return
            bstack1llll1111ll_opy_ = {bstack11l1l11_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᅫ"): status.lower()}
            bstack1llll1l1111_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll1ll1_opy_, None)
            if status.lower() == bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᅬ") and bstack1llll1l1111_opy_ is not None:
                bstack1llll1111ll_opy_[bstack11l1l11_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᅭ")] = bstack1llll1l1111_opy_[0][bstack11l1l11_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᅮ")][0] if isinstance(bstack1llll1l1111_opy_, list) else str(bstack1llll1l1111_opy_)
            driver.execute_script(
                bstack11l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᅯ").format(
                    json.dumps(
                        {
                            bstack11l1l11_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅰ"): bstack11l1l11_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅱ"),
                            bstack11l1l11_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅲ"): bstack1llll1111ll_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1l1l1l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1l1l1ll_opy_, True)
    @measure(event_name=EVENTS.bstack1ll1ll11ll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1lll11l11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᅳ")).get(bstack11l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᅴ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11l1l1l_opy_, None)
            if not test_name:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᅵ"))
                return
            bstack1lll111ll1l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, [])
            if not bstack1lll111ll1l_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᅶ") + str(bstack11111111l1_opy_) + bstack11l1l11_opy_ (u"ࠧࠨᅷ"))
                return
            for bstack1lll111ll11_opy_, bstack1lll11l1l11_opy_ in bstack1lll111ll1l_opy_:
                if not bstack1llllll11l1_opy_.bstack1lll11l1lll_opy_(bstack1lll11l1l11_opy_):
                    continue
                driver = bstack1lll111ll11_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᅸ").format(
                        json.dumps(
                            {
                                bstack11l1l11_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅹ"): bstack11l1l11_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᅺ"),
                                bstack11l1l11_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅻ"): {bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᅼ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1l1l1l_opy_(instance, bstack1lll111lll1_opy_.bstack1llll11lll1_opy_, True)
    def bstack1llll111lll_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        f: TestFramework,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll1ll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        bstack1lll111ll1l_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, [])]
        if not bstack1lll111ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦᅽ"))
            return
        if not bstack1llll11llll_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᅾ"))
            return
        for bstack1lll111llll_opy_ in bstack1lll111ll1l_opy_:
            driver = bstack1lll111llll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11l1l11_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦᅿ") + str(timestamp)
            driver.execute_script(
                bstack11l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆀ").format(
                    json.dumps(
                        {
                            bstack11l1l11_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆁ"): bstack11l1l11_opy_ (u"ࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦᆂ"),
                            bstack11l1l11_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆃ"): {
                                bstack11l1l11_opy_ (u"ࠦࡹࡿࡰࡦࠤᆄ"): bstack11l1l11_opy_ (u"ࠧࡇ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠤᆅ"),
                                bstack11l1l11_opy_ (u"ࠨࡤࡢࡶࡤࠦᆆ"): data,
                                bstack11l1l11_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࠨᆇ"): bstack11l1l11_opy_ (u"ࠣࡦࡨࡦࡺ࡭ࠢᆈ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1l11lll_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        f: TestFramework,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll1ll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        keys = [
            bstack1lll111lll1_opy_.bstack1llll11l11l_opy_,
            bstack1lll111lll1_opy_.bstack1lll1llllll_opy_,
        ]
        bstack1lll111ll1l_opy_ = []
        for key in keys:
            bstack1lll111ll1l_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll111ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡴࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣࡸࡴࠦ࡬ࡪࡰ࡮ࠦᆉ"))
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll111111_opy_, False):
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡈࡈࡔࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡦࡶࡪࡧࡴࡦࡦࠥᆊ"))
            return
        self.bstack1llllllll11_opy_()
        bstack1l11lll1l_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1ll111_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1111l_opy_)
        req.test_framework_state = bstack11111111l1_opy_[0].name
        req.test_hook_state = bstack11111111l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11l1ll_opy_)
        for bstack1lll111ll11_opy_, driver in bstack1lll111ll1l_opy_:
            try:
                webdriver = bstack1lll111ll11_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠦ࡜࡫ࡢࡅࡴ࡬ࡺࡪࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠣࠬࡷ࡫ࡦࡦࡴࡨࡲࡨ࡫ࠠࡦࡺࡳ࡭ࡷ࡫ࡤࠪࠤᆋ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦᆌ")
                    if bstack1llllll11l1_opy_.get_state(driver, bstack1llllll11l1_opy_.bstack1lll11lll11_opy_, False)
                    else bstack11l1l11_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠧᆍ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llllll11l1_opy_.get_state(driver, bstack1llllll11l1_opy_.bstack1lll1l1l11l_opy_, bstack11l1l11_opy_ (u"ࠢࠣᆎ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llllll11l1_opy_.get_state(driver, bstack1llllll11l1_opy_.bstack1lll1l11ll1_opy_, bstack11l1l11_opy_ (u"ࠣࠤᆏ"))
                caps = None
                if hasattr(webdriver, bstack11l1l11_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᆐ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤࡩ࡯ࡲࡦࡥࡷࡰࡾࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠲ࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆑ"))
                    except Exception as e:
                        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠯ࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠺ࠡࠤᆒ") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨᆓ"))
                try:
                    bstack1lll11l11ll_opy_ = json.dumps(caps).encode(bstack11l1l11_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆔ")) if caps else bstack1lll11ll1l1_opy_ (u"ࠢࡼࡿࠥᆕ")
                    req.capabilities = bstack1lll11l11ll_opy_
                except Exception as e:
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡤࡩࡢࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣࡷࡪࡸࡩࡢ࡮࡬ࡾࡪࠦࡣࡢࡲࡶࠤ࡫ࡵࡲࠡࡴࡨࡵࡺ࡫ࡳࡵ࠼ࠣࠦᆖ") + str(e) + bstack11l1l11_opy_ (u"ࠤࠥᆗ"))
            except Exception as e:
                self.logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡤࡳ࡫ࡹࡩࡷࠦࡩࡵࡧࡰ࠾ࠥࠨᆘ") + str(str(e)) + bstack11l1l11_opy_ (u"ࠦࠧᆙ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111ll1l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, [])
        if not bstack1llll11llll_opy_() and len(bstack1lll111ll1l_opy_) == 0:
            bstack1lll111ll1l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll111ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆚ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠨࠢᆛ"))
            return {}
        if len(bstack1lll111ll1l_opy_) > 1:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆜ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠣࠤᆝ"))
            return {}
        bstack1lll111ll11_opy_, bstack1lll1l11l11_opy_ = bstack1lll111ll1l_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆞ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠥࠦᆟ"))
            return {}
        capabilities = f.get_state(bstack1lll1l11l11_opy_, bstack1llllll11l1_opy_.bstack1lll1ll1l1l_opy_)
        if not capabilities:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆠ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᆡ"))
            return {}
        return capabilities.get(bstack11l1l11_opy_ (u"ࠨࡡ࡭ࡹࡤࡽࡸࡓࡡࡵࡥ࡫ࠦᆢ"), {})
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111ll1l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, [])
        if not bstack1llll11llll_opy_() and len(bstack1lll111ll1l_opy_) == 0:
            bstack1lll111ll1l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll111ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆣ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠣࠤᆤ"))
            return
        if len(bstack1lll111ll1l_opy_) > 1:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆥ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠥࠦᆦ"))
        bstack1lll111ll11_opy_, bstack1lll1l11l11_opy_ = bstack1lll111ll1l_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆧ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᆨ"))
            return
        return driver